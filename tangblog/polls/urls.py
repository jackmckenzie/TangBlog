from django.conf.urls import pattersn, url

from polls import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
)


