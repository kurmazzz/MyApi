from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    name = models.CharField(max_length=255)
    git_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    date = models.DateField(blank=True, default="2020-01-01")
