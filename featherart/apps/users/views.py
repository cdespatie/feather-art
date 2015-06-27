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
        # TODO: Check a username already exists.
        # TODO: Check if email already registered?
        
        # Create a new INNACTIVE user
        user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
        user.is_active = False;
        user.save()

        # Send activation email
        send_mail('FeatherArt Registration',
            'Please register using: ' +
            str(user.useractivation.activation_id),
            'from@example.com',
            [str(user.email)],
            fail_silently=False)

        # Return success page
        return render_to_response(
            'users/register_success.html',
            self.get_context_data(form=form)
        )

class ActivateView(View):
    # TODO: Stop user from re-activating an active account (all this does is reset date)
    template_name = 'users/activate.html'
    form_class = ActivateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Process data
            form.process()

            return HttpResponseRedirect('/activate/success')

        return render(request, self.template_name, {'form': form})
