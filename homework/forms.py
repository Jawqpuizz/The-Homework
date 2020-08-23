from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# we create extended field here and we can call this customize form


class registerForm(UserCreationForm):
    email = forms.EmailField()
    role =forms.ChoiceField(choices=[
        ('student', 'Students'),('teacher','Teacher')
    ], required= True)

    class Meta:
        model = User
        fields = ["role","username","email","password1","password2"]

