from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'game.views.home', name='home'),
    url(r'^game/$', 'game.views.game', name='game'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^play/(\d)$','game.views.play', name='play'),
    url(r'^add1/(\d)$','game.views.add1',name='add1'),
    url(r'^add2/$','game.views.add2', name='add2'),
    url(r'^clear/$','game.views.clear', name='clear'),
    url(r'^modo/$','game.views.modo', name='modo'),
    url(r'^games/$','game.views.games', name='games'),
    url(r'^plays/(\d)$','game.views.plays', name='plays'),
    url(r'^admin/', include(admin.site.urls)),
)
