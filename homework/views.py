from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import HomeworkForm, SubmissionForm
from .models import UserRegister, HomeworkList, Homeworkfeedback,MyUserAuth
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User,auth


def home(request):
    return render(request, 'index.html', {})


# Create your views here.
def signup(request):
    #tried to used form but it did not save it for me
    if request.method == 'POST':      
        role = request.POST.get('userrole')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                message = "This username is already taken"
                return render(request,'signup.html',{'message':message})
            elif User.objects.filter(email = email).exists():
                message = "This email is already taken"
                return render(request,'signup.html',{'message':message}) 
            else:                                                                                    #use this field as a placeholder
                user = User.objects.create_user(username=username,email = email,password = password1,first_name = role)
                user.save()
                return redirect('/login/')
        else:
            message = "Passwords don't match!!"    
            return render(request,'signup.html',{'message':message})
            
    else:
        return render(request, 'signup.html', {})

#----------login page---------------
def login_page(request):
    if request.method == "POST":   
            email = request.POST.get('email')
            password =  request.POST.get('password') 
            username = User.objects.get(email=email).username
            user = auth.authenticate(username = username, password=password)
            
            if user is not None:
                auth.login(request,user)
                if user.first_name == 'Student':
                    #later find the way to send username for the page
                    return redirect('/student/'+user.username)
                else:
                    return redirect('/teacher/'+user.username)
            else:
                message = "Invalid User or Password"
                return render(request, 'registration/login.html', {'message':message})
    else:
        return render(request, 'registration/login.html',{})

#----------teacher page---------------#


def teachers(request,username):
    return render(request, 'teachers.html', {'username':username})


def students(request,username):
    return render(request, 'students.html', {'username':username})

#------------Homwork list for student-------------
def homeworkList(request,username):
    if request.method == "POST":
        result = request.POST.get('upload')
        if result:
            info = [x.strip() for x in result.split(',')]
            hwId = info[0]
            hwName = info[1]
            hwTeacher = info[2]
            try:
                return redirect('submit/'+hwId+'~'+hwName+'~'+hwTeacher+'/')
            except:
                return result(request,'404.html')

    else:
        homework = HomeworkList.objects.all()
        return render(request, 'list.html', {'homework':homework
    ,'username':username})
#------------------------------------------------
def upload(request,username):
    if request.method == "POST":
        form = HomeworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/teacher/'+username)
        else:
            return render(request,'404.html')
    else:
        form = HomeworkForm(initial={"creator_name": username})
        #to hide the udername field but want to have it because we wan to save this field in to database
        form.fields['creator_name'].widget = forms.HiddenInput()
    return render(request, 'upload.html',{'form':form})  
#-------------------------------------------


def hw_submit(request,username,info):
    info = [x.strip() for x in info.split('~')]
    if request.method == "POST":
        uploadInfo = Homeworkfeedback()
        uploadInfo.hw_id = request.POST.get('hw_id')
        uploadInfo.hw_name =  request.POST.get('hw_name')
        uploadInfo.hw_file = request.FILES.get('hw_file')
        uploadInfo.status = 1
        uploadInfo.student_notes =  request.POST.get('notes')
        uploadInfo.creator = username
        uploadInfo.teacher_name =  request.POST.get('teacher_name') 
        uploadInfo.save()   
        return redirect('/student/'+username+'/')
    else:    
        return render(request,'hwSubmit.html',{
        'hwId':info[0],'hwName':info[1],'hwTeacher':info[2]
        })

#-----------------------------------------------------------
def logout_page(request):
    auth.logout(request)
    return redirect('/login/')
#----------------------------------------------------------
def feedback_list(request,role,username):
    
    if role == 'Student' or role == 'student':
        feedback = Homeworkfeedback.objects.filter(creator = username)
        if feedback:
            print('yes')
            return render(request, 'fb_list.html', {'feedback':feedback
            ,'username':username})

    elif role == 'Teacher' or role == 'teacher':
        feedback = Homeworkfeedback.objects.filter(teacher_name = username)
        return render(request, 'fb_list.html', {'feedback':feedback
    ,'username':username})

    else: 
        return render(request,'404.html') 
#-----------------------------------------------------------
def error404(request,exception):
    return render(request, '404.html', status=404)

    
