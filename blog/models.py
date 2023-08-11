from django.conf import settings
from django.db import models

# Create your models here.


class Sprite:
    health = 100
    posx = 50
    posy = 50
    yspeed = 0
    xspeed = 0


class Enemy(models.Model):
    health = models.PositiveIntegerField(default=50)
    posx = models.IntegerField(default=0)
    posy = models.IntegerField(default=0)
    yspeed = models.IntegerField(default=0)
    xspeed = models.IntegerField(default=0)


class Bullet(models.Model):
    damage = models.PositiveIntegerField(default=5)
    posx = models.IntegerField(default=0)
    posy = models.IntegerField(default=0)
    yspeed = models.IntegerField(default=0)
    xspeed = models.IntegerField(default=0)
