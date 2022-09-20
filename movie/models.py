from django.db import models

class UserList(models.Model):
    username=models.CharField(max_length=100)
    movieinfo=models.CharField(max_length=100)

