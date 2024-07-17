from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    
class Players(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    reyting = models.IntegerField()
    country = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Turnamet(models.Model):
    name = models.CharField(max_length=100, unique=True)
    started = models.DateTimeField()
    end = models.DateTimeField()
    join_players = models.ManyToManyField(Players)
    
    def __str__(self) -> str:
        return self.name
    
class Match(models.Model):
    turnamet = models.ForeignKey(Turnamet, on_delete=models.CASCADE)
    round_number = models.IntegerField()
    players_one = models.ForeignKey(Players, related_name='player_one', on_delete=models.CASCADE)
    players_two = models.ForeignKey(Players, related_name='player_two', on_delete=models.CASCADE)
    results = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.turnamet.name