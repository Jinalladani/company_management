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
from userapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

    path('companyList', views.companyList, name="companyList"),
    path('addCompany', views.addCompany, name="addCompany"),
    path('editCompany/<int:id>', views.editCompany, name="editCompany"),
    path('deleteCompany/<int:id>', views.deleteCompany, name="deleteCompany"),

    path('certificateList', views.certificateList, name="certificateList"),
    path('addCertificate', views.addCertificate, name="addCertificate"),
    path('editCertificate/<int:id>', views.editCertificate, name="editCertificate"),
    path('deleteCertificate/<int:id>', views.deleteCertificate, name="deleteCertificate"),

    path('statusList', views.statusList, name="statusList"),
    path('addStatus', views.addStatus, name="addStatus"),
    path('editStatus/<int:id>', views.editStatus, name="editStatus"),
    path('deleteStatus/<int:id>', views.deleteStatus, name="deleteStatus"),

    path('ConsultantClientList', views.ConsultantClientList, name="ConsultantClientList"),
    path('addConsultantClient', views.addConsultantClient, name="addConsultantClient"),

    path('upload', views.upload, name="upload"),
    path('simple_uploadConsultantClient', views.simple_uploadConsultantClient, name="simple_uploadConsultantClient"),
    path('editConsulClient/<int:id>', views.editConsulClient, name="editConsulClient"),
    path('delConsulClient/<int:id>', views.delConsulClient, name="delConsulClient"),
    path('export_csv', views.export_csv, name="export_csv"),

    path('my_scheduleMail', views.my_scheduleMail, name="my_scheduleMail"),

    path('userSetting', views.userSetting, name="userSetting"),
    path('generateOTP', views.generateOTP, name="generateOTP"),
    path('authentication', views.authentication, name="authentication"),
    path('signup', views.signup, name="signup"),

    path('send_message/<mobileNumber>',views.send_message,name="send_message"),
    path('fatchFCM',views.fatchFCM,name="fatchFCM"),
    path('addIphoneUser/<int:id>',views.addIphoneUser,name="addIphoneUser"),
    path('sendFCMUser/<int:id>',views.sendFCMUser,name="sendFCMUser"),



]
