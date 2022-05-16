"""company_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from adminapp import views

urlpatterns = [
    path('adminLogin',views.adminLogin,name="adminLogin"),
    path('dashbord',views.dashbord,name="dashbord"),
    path('adminlogout',views.adminlogout,name="adminlogout"),

    path('clientList',views.clientList,name="clientList"),
    path('addClient',views.addClient,name="addClient"),
    path('editClient/<int:id>',views.editClient,name="editClient"),

    path('allUser',views.allUser,name="allUser"),
    path('sendFCM/<int:id>',views.sendFCM,name="sendFCM"),

    path('uSetting',views.uSetting,name="uSetting"),
    path('adduSetting',views.adduSetting,name="adduSetting"),

    path('appData_list',views.appData_list, name="appData_list"),
    path('editappData/<int:id>',views.editappData, name="editappData"),
    path('addNewaddData', views.addNewaddData, name="addNewaddData"),


]
