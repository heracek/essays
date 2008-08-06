from django.conf.urls.defaults import *

# Uncomment this for admin:
from django.contrib import admin

# Uncomment to load INSTALLED_APPS admin.py module for default AdminSite instance.
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^', include('essays.apps.essay.urls')),
)
