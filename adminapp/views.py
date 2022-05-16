import urllib
from random import randint

from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from userapp.models import *


# Create your views here


def adminLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
        return redirect('dashbord')
    return render(request, 'adminLogin.html')


def dashbord(request):
    return render(request, 'dashbord.html')


def adminlogout(request):
    logout(request)
    return redirect('login')


def clientList(request):
    allClient = client.objects.all()
    print(allClient)
    return render(request, 'clientList.html', {'allClient': allClient})


def addClient(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        PhoneNo = request.POST['phone_no']

        client.objects.create(username=username, email=email, password=password, PhoneNo=PhoneNo)
        # sendmail("Authentication", "mail_authenticationTemplate", email,
        #          {'email': email, 'password': password})
        return redirect('clientList')
    return render(request, 'addClient.html')


def sendmail(subject, template, to, context, lookup_kwargs=None):
    email_user = AppData.objects.get(key="EMAIL_HOST_USER")

    template_str = template + '.html'
    html_message = render_to_string(template_str, {'data': context})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, email_user, [to], html_message=html_message)


def editClient(request,id):
    editClient = client.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        PhoneNo = request.POST['PhoneNo']

        editClient.username = username
        editClient.email = email
        editClient.PhoneNo = PhoneNo
        editClient.save()
        return redirect('clientList')
    return render(request, 'editClient.html',{'editClient':editClient})


def allUser(request):
    userList = AndroidSetting.objects.all()
    return render(request,'allUser.html',{'userList':userList})


def sendFCM(request,id):
    FCMUser = AndroidSetting.objects.get(id=id)
    return render(request, 'sendFCM.html', {'FCMUser': FCMUser})


def appData_list(request):
    appdata = AppData.objects.all()
    return render(request, 'appData.html', {'appdata': appdata})


def addNewaddData(request):
    if request.method == "POST":
        key = request.POST['key']
        value = request.POST['value']

        AppData.objects.create(key=key, value=value)
        return redirect('appData_list')

    return render(request, 'addNewaddData.html')


def editappData(request, id):
    appdata = AppData.objects.get(id=id)
    if request.method == "POST":
        key = request.POST['key']
        value = request.POST['value']
        appdata.key = key
        appdata.value = value
        appdata.save()
        return redirect('appData_list')

    return render(request, 'editappData.html', {'appdata': appdata})


def uSetting(request):
    notifactionSetting = NotifactionSetting.objects.all()
    return render(request,'uSetting.html',{'notifactionSetting':notifactionSetting})


def adduSetting(request):
    if request.method == 'POST':
        nList = request.POST['service']
        NotifactionSetting.objects.create(nList=nList)
        return redirect('uSetting')
    return render(request,'uSetting.html')