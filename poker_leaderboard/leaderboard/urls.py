# leaderboard/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('players', views.PlayerViewSet, basename='player')
router.register('games', views.GameViewSet, basename='game')
router.register('buy-ins', views.BuyInViewSet, basename='buyin')
urlpatterns = [
    path('', views.leaderboard_view, name='leaderboard'),
    path('api/', include(router.urls)),
    path('start-game/', views.start_game, name='start_game'),

]