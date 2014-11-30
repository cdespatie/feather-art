from django.shortcuts import render_to_response
from users.forms import UserForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core.mail import send_mail


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserForm
    model = User
    success_url = '/users/success/'

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
            'users/register_success.html',
            self.get_context_data(form=form)
        )
