from django.conf import settings
from django.db import models

# Create your models here.


class Sprite(models.Model):
    health = models.PositiveIntegerField(default=100)
    posx = models.IntegerField(default=0)
    posy = models.IntegerField(default=0)
    yspeed = models.IntegerField(default=0)
    xspeed = models.IntegerField(default=0)


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
