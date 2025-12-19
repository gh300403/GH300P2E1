from django.contrib import admin
from .models import Team, Activity, Leaderboard, Workout

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id','user','activity_type','duration','team')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('id','user','team','points')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id','name','difficulty')
