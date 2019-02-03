from django.db import models


# Create your models here.


class Battle(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    year = models.IntegerField()
    attacker_king = models.CharField(max_length=500)
    defender_king = models.CharField(max_length=500)
    attacker_1 = models.CharField(max_length=500)
    attacker_2 = models.CharField(max_length=500)
    attacker_3 = models.CharField(max_length=500)
    attacker_4 = models.CharField(max_length=500)
    defender_1 = models.CharField(max_length=500)
    defender_2 = models.CharField(max_length=500)
    defender_3 = models.CharField(max_length=500)
    defender_4 = models.CharField(max_length=500)
    attacker_outcome = models.CharField(max_length=10)
    battle_type = models.CharField(max_length=100)
    major_death = models.IntegerField()
    major_capture = models.IntegerField()
    attacker_size = models.IntegerField()
    defender_size = models.IntegerField()
    attacker_commander = models.CharField(max_length=500)
    defender_commander = models.CharField(max_length=500)
    summer = models.IntegerField()
    location = models.CharField(max_length=500)
    region = models.CharField(max_length=500)
    note = models.CharField(max_length=500)
