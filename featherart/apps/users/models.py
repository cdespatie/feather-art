from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from datetime import datetime


class UserActivation(models.Model):
    user = models.OneToOneField(User)
    activation_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    is_activated = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now)
    date_activated = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.user.username


def create_user_activation(sender, instance, created, **kwargs):
    if created:
        UserActivation.objects.create(user=instance)

post_save.connect(create_user_activation, sender=User)
