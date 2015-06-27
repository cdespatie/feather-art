from django import forms
from django.contrib.auth.models import User
from users.models import UserActivation
from datetime import datetime


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

        # Grab data for user activation
        clean_data = self.cleaned_data
        ua = UserActivation.objects.get(activation_id=clean_data['activation_key']) # Grab user activation row
        
        # Set activated flag & update date
        ua.is_activated = True 
        ua.activated_date = datetime.now 
        ua.user.is_active = True # Set user object to active

        # Save both user and user activation objects
        ua.user.save()
        ua.save()

