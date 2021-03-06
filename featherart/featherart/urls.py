from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'featherart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^submission/', include('submission.urls')),
    url(r'^accounts/', include('users.urls'))
)
# This is for serving static user uploaded images from dev environment
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
