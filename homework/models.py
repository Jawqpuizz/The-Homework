from django.db import models




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




