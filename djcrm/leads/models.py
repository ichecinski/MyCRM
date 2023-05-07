from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    company = models.CharField(max_length=50)
    agent = models.ForeignKey("leads.Agent", on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

