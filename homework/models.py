from django.db import models


# Create your models here.
class InsertNewUser(models.Model):
    user_role = models.CharField(max_length=25)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "users"
