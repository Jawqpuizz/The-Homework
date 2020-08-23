from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login, name='login'),
    path('signup/',views.signup,name='signup'),
    path('teacher/<str:username>', views.teachers, name = 'teacher'),
    path('student/<str:username>', views.students, name='student'),


]