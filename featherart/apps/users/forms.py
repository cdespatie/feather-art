from django import forms
from django.contrib.auth.models import User
from users.models import UserActivation


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ActivateForm(forms.Form):
    activation_key = forms.UUIDField()

    # Activates a user in the database.
    def process(self):
        # This should only be called after form.is_valid()
        clean_data = self.cleaned_data
        ua = UserActivation.objects.get(activation_id=clean_data['activation_key']) # Grab user activation row
        ua.is_activated = True
        ua.save()

