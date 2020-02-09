from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission


class GoalStatus(models.Model):
    status_name     = models.CharField(max_length=120)

    def __str__(self):
        return self.status_name



class ScrumyGoals(models.Model):
    goal_name       = models.CharField(max_length=121)
    goal_id         = models.IntegerField(default=0.00)
    created_by      = models.CharField(max_length=120)
    moved_by        = models.CharField(max_length=120)
    owner           = models.CharField(max_length=120)
    goal_status     = models.ForeignKey(GoalStatus, on_delete=models.PROTECT, null=True)
    user            = models.ForeignKey(User, on_delete=models.CASCADE,
                         related_name= 'User_profile', null=True)

    def __str__(self):
        return self.goal_name



class ScrumyHistory(models.Model):
    moved_by        = models.CharField(max_length=120)
    created_by      = models.CharField(max_length=120)
    moved_from      = models.CharField(max_length=120)
    moved_to        = models.CharField(max_length=120)
    time_of_action  = models.DateTimeField()
    goal            = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by







