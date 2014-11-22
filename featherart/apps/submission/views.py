#from django.shortcuts import render
from django.views import generic

from submission.models import Submission


class SubmissionView(generic.DetailView):
    model = Submission
    template_name = 'submission/submission_detail.html'
