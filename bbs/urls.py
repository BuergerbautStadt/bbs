from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView,RedirectView
from django.contrib import admin

from wbc.process.views import PublicationFeed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='core/map.html')),
    url(r'^begriffe/$', 'wbc.process.views.process'),
    url(r'^liste/$', TemplateView.as_view(template_name='process/list.html')),

    # orte
    url(r'^orte/$', RedirectView.as_view(url='/liste/', permanent=True)),
    url(r'^orte/(?P<pk>\d+)/$', 'wbc.process.views.place'),

    # veroeffentlichungen neu
    url(r'^veroeffentlichungen/neu/$', 'wbc.process.views.create_publication'),

    # feeds
    url(r'^feeds/$', 'wbc.core.views.feeds'),
    url(r'^veroeffentlichungen/feed/$', PublicationFeed(), name="publication_feed_url"),

    # news module
    url(r'^news/abonnieren/$', 'wbc.news.views.subscribe'),
    url(r'^news/abbestellen/(?P<email>.*)$', 'wbc.news.views.unsubscribe'),
    url(r'^news/validieren/(?P<code>.*)$', 'wbc.news.views.validate'),

    # region and process modules, urls by djangorestframework, do not change
    url(r'^region/', include('wbc.region.urls')),
    url(r'^process/', include('wbc.process.urls')),

    # admin foo
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # user login
    # url(r'^login/', 'wbc.core.views.login_user'),
    # url(r'^logout/', 'wbc.core.views.logout_user'),

    # robots.txt and sitemap.xml
    (r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    (r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/plain')),
)
