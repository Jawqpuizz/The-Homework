from django.shortcuts import render
from homework.models import InsertNewUser
from django.contrib import messages


def home(request):
    return render(request, 'index.html', {})


# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST.get('userrole') and request.POST.get('username') and request.POST.get(
                'email') and request.POST.get('password'):
            save_record = InsertNewUser()
            save_record.userrole = request.POST.get('userrole')
            save_record.username = request.POST.get('username')
            save_record.email = request.POST.get('email')
            save_record.password = request.POST.get('password')
            save_record.save()
            messages.success(request, 'You are successfully registered')
            if request.POST.get('userrole') == 'Student':
                return render(request, 'students.html',{'username':request.POST.get('username')})
            else:
                return render(request, 'teachers.html',{'usernamr': request.POST.get('username')})
    else:
            return render(request, 'signup.html', {})


def login(request):
    return render(request, 'login.html', {})


def teachers(request):
    return render(request, 'teachers.html', {})


def students(request):
    return render(request, 'students.html', {})
