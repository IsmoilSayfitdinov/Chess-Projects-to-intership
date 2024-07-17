from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path("users/", UserListAPIView.as_view()),
    path("users/<int:pk>/", UserDetailAPIView.as_view()),
    
    path("players/", PlayersListAPIView.as_view()),
    path("players/<int:pk>/", PlayerDetailAPIView.as_view()),
    
    path("turnamets/", TurnametListAPIView.as_view()),
    path("turnamets/<int:pk>/", TurnametDetailAPIView.as_view()),
    path('tournaments/<int:pk>/leaderboard/', leaderboard, name='tournament_leaderboard'),
    
    path("matches/", MatchListAPIView.as_view()),
    path("matches/<int:pk>/", MatchDetaliAPIView.as_view()),
    
    path("token/", TokenObtainPairView.as_view()),
    path("register/", RegisterAPiView.as_view()),
]