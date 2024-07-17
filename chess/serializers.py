from rest_framework import serializers
from .models import User, Players, Turnamet, Match


class UserSerializers(serializers.ModelSerializer):
     class Meta:
        model = User 
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user
        
        
class PlayersSerilizers(serializers.ModelSerializer):
     class Meta:
        model = Players 
        fields = '__all__'
class TurnametSerilizers(serializers.ModelSerializer):
     class Meta:
        model = Turnamet
        fields = '__all__'
        
class MatchSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Match 
        fields = '__all__'