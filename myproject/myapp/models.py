# myapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    assigned_users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name
