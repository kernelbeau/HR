from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from project.views import Index

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^hr/', include('human_res.urls', namespace='human_res')),
)

if settings.MY_HOST in settings.DEV_SERV:
    urlpatterns += staticfiles_urlpatterns()

    # debug_toolbar settings
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
