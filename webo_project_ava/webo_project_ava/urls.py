from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'webo_project_ava.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gamestore.views.starting_site'),
    url(r'^login/$', 'gamestore.views.login'),
    url(r'^auth/$', 'gamestore.views.auth_view'),
    url(r'^logout/$', 'gamestore.views.logout'),
    url(r'^loggedin/$', 'gamestore.views.loggedin'),
    url(r'^invalid/$', 'gamestore.views.invalid_login'),
    url(r'^register/$', 'gamestore.views.register_user'),
    url(r'^register_confirmation/$', 'gamestore.views.confirm_required'),
    url(r'^register_success/$', 'gamestore.views.register_success'),
    url(r'^confirm/(?P<activation_key>\w+)/', 'gamestore.views.register_confirm'),
    url(r'^games/$', 'gamestore.views.games'),
    url(r'^games/(?P<game_id>\d+)/$', 'gamestore.views.game'),
    url(r'^addgame/$', 'gamestore.views.addgame'),
    url(r'^deletegame/(?P<game_id>\d+)/$', 'gamestore.views.delete_game'),
    url(r'^profile/$', 'gamestore.views.profile'),
    url(r'^update_profile/$', 'gamestore.views.update_profile'),
    url(r'^update_success/$', 'gamestore.views.update_success'),
    url(r'^games/(?P<game_id>\d+)/update_game/$', 'gamestore.views.update_game'),
    url(r'^submit_highscore/$', 'gamestore.views.submit_highscore'),
    url(r'^save_state/$', 'gamestore.views.save_state'),
    url(r'^load_state/$', 'gamestore.views.load_state'),
]
