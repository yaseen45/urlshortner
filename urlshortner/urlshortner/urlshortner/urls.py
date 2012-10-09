from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
     url(r'^assign/', 'shortner.views.search_assign',name='search_assign'),
     url(r'^$', 'shortner.views.index',name='index'),
     url(r'^(P<shortt>\w+)/$', 'shortner.views.goto',name='goto'),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static_media/(?P<path>.*)$', 'django.views.static.serve', {
             'document_root': settings.MEDIA_ROOT,
        }),
   )
