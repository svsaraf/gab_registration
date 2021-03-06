from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gab.views.register', name='index'),
    # url(r'^myapp/', include('myapp.foo.urls')),
    url(r'^tango/', include('tango.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^register/', 'gab.views.register', name='register'),
    url(r'^login/', 'gab.views.user_login', name='login'),
    url(r'^logout/', 'gab.views.user_logout', name='logout'),
)
