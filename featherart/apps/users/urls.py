from django.conf.urls import url, patterns
from users.views import RegisterView, ActivateView
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import user_passes_test

# Redirect to homepage if user tries to access login page while already logged in.
login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), '/')

urlpatterns = patterns('',
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^activate/$', ActivateView.as_view(), name='activate'),
    url(r'^login/$', login_forbidden(login), {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'users/logout.html', 'next_page':'/'}, name='logout')
)
