from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAdminUser]
    
    
class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAdminUser]

class RegisterAPiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  
  
class PlayersListAPIView(generics.ListCreateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerilizers
    permission_classes = [permissions.IsAuthenticated]
    
class PlayerDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerilizers
    permission_classes = [permissions.IsAuthenticated]

class TurnametListAPIView(generics.ListCreateAPIView):
    queryset = Turnamet.objects.all()
    serializer_class = TurnametSerilizers
    permission_classes = [permissions.IsAuthenticated]


class TurnametDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Turnamet.objects.all()
    serializer_class = TurnametSerilizers
    permission_classes = [permissions.IsAuthenticated]
    
    
class MatchListAPIView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerilizers
    permission_classes = [permissions.IsAuthenticated]

class MatchDetaliAPIView(generics.RetrieveUpdateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerilizers
    permission_classes = [permissions.IsAuthenticated]
    
    
    
    
@api_view(['GET'])
def leaderboard(request, pk):
    turnamet = Turnamet.objects.get(id=pk)
    matches = Match.objects.filter(turnamet=turnamet, results_isnull = False)
    
    leaderboard = []
    for match in matches:
        if match.players_one_id not in leaderboard:
            leaderboard[match.players_one_id] = {
                "player": match.players_one.name,
                "points": 0
            }
        if match.players_two_id not in leaderboard:
            leaderboard[match.players_two_id] = {
                "player": match.players_one.name,
                "points": 0
            }
        
        if match.results == "player_one_win":
            leaderboard[match.players_one_id]["points"] += 1
        elif match.results == "player_two_win":
            leaderboard[match.players_two_id]["points"] += 1
        
    sorted_leader = sorted(leaderboard.valuse(), key=lambda x: x["points"], reverse=True)
    return Response(sorted_leader)   
        