from django.db import models
import os
import uuid


# We write all submission paths to include a UUID to guarantee uniqueness.
def get_file_path(instance, filename):
    return os.path.join('submissions', 'username', str(uuid.uuid4()) + "_" + filename)


class Submission(models.Model):
    content_path = models.FileField(upload_to=get_file_path)
    title = models.CharField(max_length=200)
    date_submitted = models.DateTimeField()
    description = models.CharField(max_length=2000)
    content_rating = models.IntegerField()

    def __unicode__(self):
        """Important to add these in Django!"""
        return self.title
