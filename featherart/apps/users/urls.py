from django.conf.urls import url, patterns

from users import views

urlpatterns = patterns('',
    url(r'^register/$', views.register, name='register')
)
