"""Hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from HSPTL.views import CreateDoctor, DoctorList,DetailDoctor,DoctorUpdate, edit_doctor, get_doctor, homepage, get_data, edit_data, get_owner, edit_dept,get_dept

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home1/', homepage,name='home'),
    path('get_data/', get_data,name='get_data'),
    path('edit_data/<int:pk>', edit_data,name='edit_data'),
    path('get_owner/', get_owner,name='get_owner'),

    path('get_dept/', get_dept ,name='get_dept'),
    path('dept/<int:pk>', edit_dept,name='dept'),

    path('get_doctor/', get_doctor ,name='get_doctor'),
    path('doctor/<int:pk>', edit_doctor, name='doctor'),

    path('doctorCreate/', CreateDoctor.as_view() ,name='doctorCreate'),

    path('doctorList/', DoctorList.as_view() ,name='doctorList'),
    path('doctorDetail/<int:pk>', DetailDoctor.as_view() ,name='doctorDetail'),

    path('doctorUpdate/<int:pk>', DoctorUpdate.as_view() ,name='doctorUpdate'),

]

