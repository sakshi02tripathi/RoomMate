# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location_preference = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    smoking = models.CharField(max_length=10, null=True, blank=True)
    pets = models.CharField(max_length=10, null=True, blank=True)
    cleanliness = models.CharField(max_length=10, null=True, blank=True)
    sleep_schedule = models.CharField(max_length=10, null=True, blank=True)
    work_schedule = models.CharField(max_length=10, null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)
    interests = models.ManyToManyField('Interest', blank=True)

class Interest(models.Model):
    name = models.CharField(max_length=100)
