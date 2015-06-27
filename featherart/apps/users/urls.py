from django.conf.urls import url, patterns

from users.views import RegisterView, ActivateView

urlpatterns = patterns('',
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^activate/$', ActivateView.as_view(), name='activate')
)
