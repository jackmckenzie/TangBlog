from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tangblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    urls(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
