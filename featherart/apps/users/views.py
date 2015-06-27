from django.shortcuts import render_to_response, render
from users.forms import UserForm, ActivateForm
from django.views.generic import CreateView, View
from django.contrib.auth.models import User
from users.models import UserActivation
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserForm
    model = User
    success_url = '/accounts/success/'

    def form_valid(self, form):
        self.object = form.save()
        self.object.is_active = False
        self.object.save()

        send_mail('FeatherArt Registration',
            'Please register using: ' +
            str(self.object.useractivation.activation_id),
            'from@example.com',
            [str(self.object.email)],
            fail_silently=False)

        return render_to_response(
            'accounts/register_success.html',
            self.get_context_data(form=form)
        )

class ActivateView(View):
    template_name = 'users/activate.html'
    form_class = ActivateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Process DATA
            form.process()

            return HttpResponseRedirect('/activate/success')

        return render(request, self.template_name, {'form': form})
