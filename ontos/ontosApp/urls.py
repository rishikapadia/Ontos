from django.conf.urls import patterns, include, url

from ontosApp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ontos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='main'),
)







