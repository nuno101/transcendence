from django.db import models

# Create your models here.

class Tournament(models.Model):
    title = models.CharField(max_length=150)
    description= models.CharField(max_length=900)
    created_at = models.DateTimeField("creation date")


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

