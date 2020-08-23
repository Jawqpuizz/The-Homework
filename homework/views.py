from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import registerForm
from .models import UserRegister
from django.contrib import messages


def home(request):
    return render(request, 'index.html', {})


# Create your views here.
def signup(request):

    if request.method == 'POST':
        print(request.POST.get('email'))
        if request.POST.get('userrole') and request.POST.get('username') and request.POST.get(
                'email') and request.POST.get('password'):
            save_record = UserRegister()
            save_record.role = request.POST.get('userrole')
            save_record.username = request.POST.get('username')
            save_record.email = request.POST.get('email')
            save_record.password1 = request.POST.get('password')
            save_record.save()
            return redirect('/login')
            
    else:
        return render(request, 'signup.html', {})

#----------login page---------------#
def login(request):
    message = ""
    if request.method == "POST":   
        founded_row = UserRegister.objects.raw('SELECT * FROM users WHERE email = %s AND password1 = %s'
        ,[request.POST.get('email'),request.POST.get('password') ])
        print(founded_row)
        for p in founded_row: 
            if p.role == 'Student':
                #later find the way to send username for the page
                return redirect('/student/'+p.username)
            else:
                return redirect('/teacher/'+p.username)
            
                
        message = "Invalid email or password"
        return render(request,'login.html',{'message':message})
    else:
        return render(request, 'login.html', {'message':message})

#----------teacher page---------------#


def teachers(request,username):
    return render(request, 'teachers.html', {'username':username})


def students(request,username):
    return render(request, 'students.html', {'username':username})
