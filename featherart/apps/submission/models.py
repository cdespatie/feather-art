from django.db import models


class Submission(models.Model):
    content_path = models.CharField(max_length=500)
    title = models.CharField(max_length=200)
    date_submitted = models.DateTimeField()
    description = models.CharField(max_length=2000)
    content_rating = models.IntegerField()

    def __unicode__(self):
        """Important to add these in Django!"""
        return self.title
