from django.conf.urls import url, patterns

from home import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='submission')
)
