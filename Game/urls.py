# from Game.views import game_detail, game_list
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url
#
# # Name spacing
# app_name = 'Game'
#
#
# # url patterns
# urlpatterns = [
#     # url(r'^$', game_list),
#     # url(r'^(?P<pk>[0-9]+)/$', game_detail),
#
#     path('', game_list, name='all-games'),
#     path('<int:pk>/', game_detail, name='add-game'),
#
# ]

##########################################################
#
#     updated url file after modifying to class based views.
#
##########################################################


from django.conf.urls import url
from Game import views


urlpatterns = [

    url(r'^game-categories/$', views.GameCategoryList.as_view(), name=views.GameCategoryList.name),
    url(r'^game-categories/(?P<pk>[0-9]+)/$', views.GameCategoryDetail.as_view(), name=views.GameCategoryDetail.name),
    url(r'^games/$', views.GameList.as_view(), name=views.GameList.name),
    url(r'^games/(?P<pk>[0-9]+)/$', views.GameDetail.as_view(), name=views.GameDetail.name),
    url(r'^players/$', views.PlayerList.as_view(), name=views.PlayerList.name),
    url(r'^players/(?P<pk>[0-9]+)/$', views.PlayerDetail.as_view(), name=views.PlayerDetail.name),
    url(r'^player-scores/$', views.PlayerScoreList.as_view(), name=views.PlayerScoreList.name),
    url(r'^player-scores/(?P<pk>[0-9]+)/$', views.PlayerScoreDetail.as_view(), name=views.PlayerScoreDetail.name),
    url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name)
    ]
