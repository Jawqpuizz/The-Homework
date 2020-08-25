from django.db import models
import datetime

#class loginAuth(models.Manager):
 #   def login_check(self,email,password1):
 #       if UserRegister.object.filter(email == email, password1 == password1).exists():
 #           return True
 #       return False

    
# Create your models here.
class UserRegister(models.Model):   
    role = models.CharField(max_length=25)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    objects = models.Manager

    def login_check(self,email,password):
        if self.email == email and self.password1 == password:
            return True
        return False

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
    hw_id = models.IntegerField()
    datetime =models.DateField()
    file_name = models.FileField(upload_to='homework/hw_submission')
    status = models.CharField(max_length=255)
    feedback = models.CharField(max_length=255)
    creator = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    objects = models.Manager

    class Meta:
        db_table = "feedbacks"


