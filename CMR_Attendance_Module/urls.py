"""
URL configuration for CMR_Attendance_Module project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

    #login path
    path('',views.LOGIN,name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    #profile update
    path('Profile',views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),

    #this is hod panel
    path('Hod/Home', Hod_Views.HOME,name='hod_home'),
    path('Hod/Student/Add',Hod_Views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',Hod_Views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_Views.EDIT_STUDENT,name='edit_student'),
    path('Hod/Student/Update',Hod_Views.UPDATE_STUDENT,name='update_student'),
    path('Hod/Student/Delete/<str:admin>',Hod_Views.DELETE_STUDENT,name='delete_student'),
    path('Hod/Staff/View',Hod_Views.VIEW_STAFF,name='view_staff'),

    path('Hod/View/Attendance',Hod_Views.VIEW_ATTENDANCE,name='view_attendance'),



    #this is staff panel
    path('Staff/Home',Staff_Views.HOME,name='staff_home'),
    path('Staff/Take_Attendance',Staff_Views.STAFF_TAKE_ATTENDANCE,name='staff_take_attendance'),
    path('Staff/Save_Attendance',Staff_Views.STAFF_SAVE_ATTENDANCE,name='staff_save_attendance'),
    path('Staff/View_Attendance',Staff_Views.STAFF_VIEW_ATTENDANCE,name='staff_view_attendance'),




    #this is studentpanel
    path('Student/Home',Student_Views.HOME,name='student_home'),
    path('Student/View_Attendance',Student_Views.STUDENT_VIEW_ATTENDANCE,name='student_view_attendance'),





] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
