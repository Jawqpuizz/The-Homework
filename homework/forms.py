from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import HomeworkList, Homeworkfeedback


# we create extended field here and we can call this customize form

# I did not use it because I already have my login and register page before
class registerForm(UserCreationForm):
    email = forms.EmailField()
    role =forms.ChoiceField(choices=[
        ('student', 'Students'),('teacher','Teacher')
    ], required= True)

    class Meta:
        model = User
        fields = ["role","username","email","password1","password2"]


class HomeworkForm(forms.ModelForm):
    
    class Meta:
        model = HomeworkList
        fields = ("hw_name", "hw_desc", "hw_file", "creator_name")


class SubmissionForm(forms.ModelForm):

    class Meta:
        model = Homeworkfeedback
        fields = ("hw_id","status","hw_name","creator","teacher_name")