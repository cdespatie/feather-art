from django.db import models
from django.contrib.auth.models import User
import os
import uuid


class UserActivation(models.Model):
    user = models.OneToOneField(User)
    activation_id = models.CharField(max_length=100,
        blank=True, unique=True, default=uuid.uuid4)
    is_activated = models.BooleanField(default=False)

    def __unicode__(self):
        return self.activation_id
