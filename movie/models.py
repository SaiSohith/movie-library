from django.db import models

class UserList(models.Model):
    # use_in_migrations = True
    username=models.CharField(max_length=100)
    movieinfo=models.CharField(max_length=100)

