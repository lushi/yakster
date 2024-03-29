from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'yakster_app.views.index'), # root
    url(r'^login$', 'yakster_app.views.login_view'), # login
    url(r'^logout$', 'yakster_app.views.logout_view'), # logout
    url(r'^signup$', 'yakster_app.views.signup'), # signup
    url(r'^posts$', 'yakster_app.views.posts'), # posts
    url(r'^submit$', 'yakster_app.views.submit'), # submit new post
    url(r'^users/$', 'yakster_app.views.users'),
    url(r'^users/(?P<username>\w{0,30})/$', 'yakster_app.views.users'),
    url(r'^users/(?P<username>\w{0,30})/(?P<post_id>\d)/$', 'yakster_app.views.user_post'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
