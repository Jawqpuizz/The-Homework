from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login, name='login'),
    path('signup/',views.signup,name='signup'),
    path('teacher/<str:username>/', views.teachers, name = 'teacher'),
    path('student/<str:username>/', views.students, name='student'),
    path('student/<str:username>/hw_list/', views.homeworkList,name='homrworkList'),
    path('teacher/<str:username>/upload/',views.upload,name="upload"),
    path('student/<str:username>/hw_list/submit/',views.hw_submit, name="hw_submit")

]
app_name = 'homework'

#just for now
if settings.DEBUG:

    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)