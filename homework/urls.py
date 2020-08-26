from django.urls import path,re_path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (handler400, handler403, handler404, handler500)

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('signup/',views.signup,name='signup'),
    path('teacher/<str:username>/', views.teachers, name = 'teacher'),
    path('student/<str:username>/', views.students, name='student'),
    path('student/<str:username>/hw_list/', views.homeworkList,name='homrworkList'),
    path('teacher/<str:username>/upload/',views.upload,name="upload"),
   # path('student/<str:username>/hw_list/submit/<slug:info>/',views.hw_submit, name="hw_submit")
   #this url deal wil the spave of the path string
   re_path(r'^student/(?P<username>[\w|\W]+)/hw_list/submit/(?P<info>[\w|\W]+)/$', views.hw_submit, name="hw_submit"),
   path('<str:role>/<str:username>/feedback_list/',views.feedback_list,name="feedback_list"),

]


#handle page not found if users type the wrong url
handler404 = 'homework.views.error404'


#just for now
if settings.DEBUG:

    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)