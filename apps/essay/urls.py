from django.conf.urls.defaults import *
from models import HyperWord

word_info_dict = {
    'queryset': HyperWord.objects.all(),
    'slug_field': 'word',
}

urlpatterns = patterns('',
    url(r'^word/(?P<slug>\w*)/', 'django.views.generic.list_detail.object_detail', word_info_dict, name='word'),
)
