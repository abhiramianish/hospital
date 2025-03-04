"""
URL configuration for hospital_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Hosapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home_view'),
    path('register',views.patientregister.as_view(),name='reg_view'),
    path('doctorreg',views.doctorregister.as_view(),name='doc_view'),
    path('patientlst',views.patientlist.as_view(),name='list_view'),
    path('doclst',views.doctorlist.as_view(),name='doclist_view'),

    path('plist/<int:id>',views.patientedit.as_view(),name='edit_view'),
    path('pdel/<int:id>',views.patientdelete.as_view(),name='delete_view'),
    path('docedit/<int:id>',views.doctoredit.as_view(),name='docedit_view'),
    path('docdel/<int:id>',views.doctordelete.as_view(),name='docdelete_view'),
]