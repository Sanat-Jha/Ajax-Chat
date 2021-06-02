from django.db import models

# Create your models here.
class Room(models.Model):
    Name = models.CharField(max_length=1000)
    Chat = models.JSONField()