from django.db import models
from django.contrib.auth.models import User
import datetime



    
# Create your models here.
class UserRegister(models.Model):   
    role = models.CharField(max_length=25)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    is_anonymous = models.BooleanField(default=True)
    is_authenticated = models.BooleanField(default=True)
    objects = models.Manager
    class Meta:
        db_table = "users"

class HomeworkList(models.Model):
    hw_id = models.IntegerField(primary_key= True)
    datetime =models.DateField(default=datetime.datetime.now)
    hw_name = models.CharField(max_length=255)
    hw_desc = models.CharField(max_length=255)
    hw_file = models.FileField(upload_to='homework/hw_files')
    creator_name = models.CharField(max_length=100)
    objects = models.Manager

    class Meta:
        db_table = "homeworks"

#-----------------------------------
class Homeworkfeedback(models.Model):
    feedback_id = models.IntegerField(primary_key= True)
    hw_id = models.IntegerField()
    datetime =models.DateField(default=datetime.datetime.now)
    hw_name = models.CharField(max_length=255)
    hw_file = models.FileField(upload_to='homework/hw_submission')
    status = models.CharField(max_length=255)
    feedback = models.CharField(max_length=255)
    creator = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    student_notes = models.CharField(max_length=512)
    objects = models.Manager

    class Meta:
        db_table = "feedbacks"

class MyUserAuth(models.Model):   
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    objects = models.Manager
    

