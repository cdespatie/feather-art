from django.conf.urls import url, patterns

from submission import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.SubmissionView.as_view(), name='submission')
)
