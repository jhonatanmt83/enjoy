#encoding:utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'restaurant.views.home', name='home'),
    # Examples:
    # url(r'^$', 'enjoy.views.home', name='home'),
    # url(r'^enjoy/', include('enjoy.foo.urls')),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)
