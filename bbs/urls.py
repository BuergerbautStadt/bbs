from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

# from wbc.core.views import VeroeffentlichungenFeed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='core/map.html')),
    url(r'^begriffe/$', 'wbc.process.views.process'),
    url(r'^liste/$', TemplateView.as_view(template_name='process/places.html')),
    # orte
    # url(r'^orte/(?P<pk>\d+)/$', 'wbc.core.views.ort'),
    # url(r'^orte/neu/$', 'bbs.views.ort'),
    # veroeffentlichungen
    # url(r'^veroeffentlichungen/neu/$', 'wbc.core.views.create_veroeffentlichung'),
    # url(r'^veroeffentlichungen/feed/$', VeroeffentlichungenFeed(), name="feedsurl"),
    # begriffe
    # url(r'^begriffe/$', 'wbc.core.views.begriffe'),
    # feeds
    # url(r'^feeds/$', 'wbc.core.views.feeds'),
    # modules
    # url(r'^news/', include('wbc.news.urls')),
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
