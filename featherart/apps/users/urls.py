from django.conf.urls import url, patterns

from users.views import RegisterView

urlpatterns = patterns('',
    url(r'^register/$', RegisterView.as_view(), name='register')
)
