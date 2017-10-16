from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView,RedirectView
from django.contrib import admin
from django.views.static import serve

from wbc.process.views import PlaceCreate,PlaceUpdate,PlaceDelete,process,places,place
from wbc.process.views import PublicationCreate,PublicationUpdate,PublicationDelete
from wbc.process.views import PublicationFeed
from wbc.core.views import feeds
from wbc.news.views import subscribe,unsubscribe
from wbc.news.views import validate
from wbc.core.views import login_user,logout_user

admin.autodiscover()

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/map.html')),
    url(r'^begriffe/$', process, name='process'),
    url(r'^liste/$', places, name='places'),

    # orte
    url(r'^orte/$', RedirectView.as_view(url='/liste/', permanent=True)),
    url(r'^orte/neu/$', PlaceCreate.as_view(), name='place_create'),
    url(r'^orte/(?P<pk>[0-9]+)/$', place, name='place'),
    url(r'^orte/(?P<pk>[0-9]+)/bearbeiten/$', PlaceUpdate.as_view(), name='place_update'),
    url(r'^orte/(?P<pk>[0-9]+)/entfernen/$', PlaceDelete.as_view(), name='place_delete'),

    # veroeffentlichungen neu
    url(r'^veroeffentlichungen/neu/$', PublicationCreate.as_view(), name='publication_create'),
    url(r'^veroeffentlichungen/(?P<pk>[0-9]+)/bearbeiten/$', PublicationUpdate.as_view(), name='publication_update'),
    url(r'^veroeffentlichungen/(?P<pk>[0-9]+)/entfernen/$', PublicationDelete.as_view(), name='publication_delete'),

    # feeds
    url(r'^feeds/$', feeds),
    url(r'^veroeffentlichungen/feed/$', PublicationFeed(), name="publication_feed_url"),

    # news module
    url(r'^news/abonnieren/$', subscribe),
    url(r'^news/abbestellen/(?P<email>.*)$', unsubscribe),
    url(r'^news/validieren/(?P<code>.*)$', validate),

    # region and process modules, urls by djangorestframework, do not change
    url(r'^region/', include('wbc.region.urls')),
    url(r'^process/', include('wbc.process.urls')),

    # buildings
    # url(r'^buildings/(?P<pk>[0-9]+)/$', 'wbc.buildings.views.building', name='buildings'),

    # admin foo
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # user login
    url(r'^login/', login_user),
    url(r'^logout/', logout_user),

    # serve media files
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # robots.txt and sitemap.xml
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/plain')),
]

