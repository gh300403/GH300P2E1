from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, related_name='activities', on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    team = models.ForeignKey(Team, related_name='activities', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} ({self.duration}m)"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, related_name='leaderboard_entries', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='leaderboard_entries', null=True, blank=True, on_delete=models.SET_NULL)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.points} pts"

class Workout(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=50, choices=(('Easy','Easy'),('Medium','Medium'),('Hard','Hard')))

    def __str__(self):
        return self.name
