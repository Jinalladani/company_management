import csv
import time
import urllib
import urllib.parse
from datetime import timedelta, date, datetime
from random import randint

import requests
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from tablib import Dataset

from .models import *
from pyfcm import FCMNotification
from .resource import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    if 'email' in request.session:
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            uid = client.objects.get(email=email)
            print(uid)
            if uid.is_active:
                print(uid.email)
                if uid.email == email and uid.password == password:
                    print('redirect', {'user': uid})
                    request.session['id'] = uid.id
                    request.session['email'] = uid.email
                    request.session['PhoneNo'] = uid.PhoneNo
                    print(uid.PhoneNo)
                    print(uid.id)
                    return render(request, 'index.html', {'uid': uid})
        except:
            message = 'Email Invalid'
            return render(request, 'login.html', {'message': message})
        message = 'Email And Password Invalid'
        return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')


def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def companyList(request):
    if 'email' and 'id' in request.session:
        client_key = request.session['id']
        print(client_key)
        allCompany = CompanyList.objects.filter(client_key=client.objects.get(pk=client_key))
        return render(request, 'companyList.html', {'allCompany': allCompany})
    else:
        return render(request, 'login.html')


def addCompany(request):
    if 'email' and 'id' in request.session:
        client_key = request.session['id']
        if request.method == 'POST':
            name = request.POST['name']
            client_obj = client.objects.get(pk=client_key)

            CompanyList.objects.create(name=name, client_key=client_obj)
            return redirect('companyList')

        return render(request, 'addCompany.html')
    else:
        return render(request, 'login.html')


def editCompany(request, id):
    if 'email' in request.session:
        editCompany = CompanyList.objects.get(id=id)
        if request.method == 'POST':
            name = request.POST['name']

            editCompany.name = name
            editCompany.save()
            return redirect('companyList')
        return render(request, 'editCompany.html', {'editCompany': editCompany})
    else:
        return render(request, 'login.html')


def deleteCompany(request, id):
    if 'email' in request.session:
        delCompany = CompanyList.objects.get(id=id)
        delCompany.delete()
        return redirect('companyList')
    else:
        return render(request, 'login.html')


def certificateList(request):
    if 'email' and 'id' in request.session:
        client_key = request.session['id']
        print(client_key)
        allcertificate = CertificateList.objects.filter(client_key=client.objects.get(pk=client_key))
        return render(request, 'certificateList.html', {'allcertificate': allcertificate})
    else:
        return render(request, 'login.html')


def addCertificate(request):
    if 'email' and 'id' in request.session:
        client_key = request.session['id']
        if request.method == 'POST':
            certificateName = request.POST['certificateName']
            client_obj = client.objects.get(pk=client_key)

            CertificateList.objects.create(certificateName=certificateName, client_key=client_obj)
            return redirect('certificateList')

        return render(request, 'addCertificate.html')
    else:
        return render(request, 'login.html')


def editCertificate(request, id):
    if 'email' in request.session:
        editCertificate = CertificateList.objects.get(id=id)
        if request.method == 'POST':
            certificateName = request.POST['certificateName']

            editCertificate.certificateName = certificateName
            editCertificate.save()
            return redirect('certificateList')
        return render(request, 'editCertificate.html', {'editCertificate': editCertificate})
    else:
        return render(request, 'login.html')


def deleteCertificate(request, id):
    if 'email' in request.session:
        delCertificate = CertificateList.objects.get(id=id)
        delCertificate.delete()
        return redirect('certificateList')
    else:
        return render(request, 'login.html')


def statusList(request):
    if 'email' and 'id' in request.session:
        client_key = request.session['id']
        print(client_key)
        statusList = StatusList.objects.filter(client_key=client.objects.get(pk=client_key))
        return render(request, 'statusList.html', {'statusList': statusList})
    else:
        return render(request, 'login.html')


def addStatus(request):
    if 'email' and 'id' in request.session:
        client_key = request.session['id']
        if request.method == 'POST':
            name = request.POST['name']
            client_obj = client.objects.get(pk=client_key)

            StatusList.objects.create(statusList=name, client_key=client_obj)
            return redirect('statusList')

        return render(request, 'addStatus.html')
    else:
        return render(request, 'login.html')


def editStatus(request, id):
    if 'email' in request.session:
        editStatus = StatusList.objects.get(id=id)
        if request.method == 'POST':
            name = request.POST['name']

            editStatus.statusList = name
            editStatus.save()
            return redirect('statusList')
        return render(request, 'editStatus.html', {'editStatus': editStatus})
    else:
        return render(request, 'login.html')


def deleteStatus(request, id):
    if 'email' in request.session:
        delCompany = StatusList.objects.get(id=id)
        delCompany.delete()
        return redirect('statusList')
    else:
        return render(request, 'login.html')


def ConsultantClientList(request):
    if 'email' and 'id' in request.session:
        client_key = request.session['id']
        print(client_key)
        ConsultantClientList = ClientCompanyList.objects.filter(client_key=client.objects.get(pk=client_key)).order_by(
            '-id')
        return render(request, 'ConsultantClientList.html', {'ConsultantClientList': ConsultantClientList})
    else:
        return render(request, 'login.html')


def addConsultantClient(request):
    if 'email' and 'id' in request.session:
        client_key = request.session['id']
        companyList = CompanyList.objects.filter(client_key=client.objects.get(pk=client_key))
        certificateList = CertificateList.objects.filter(client_key=client.objects.get(pk=client_key))
        statusList = StatusList.objects.filter(client_key=client.objects.get(pk=client_key))
        if request.method == 'POST':
            CompantName = request.POST['CompantName']
            ClientName = request.POST['ClientName']
            PhoneNo = request.POST['PhoneNo']
            email = request.POST['email']
            city = request.POST['city']
            certificate = request.POST['certificate']
            body = request.POST['body']
            rate = request.POST['rate']
            issueDate = request.POST['issueDate']
            expiryDate = request.POST['expiryDate']
            expiryYear = request.POST['expiryYear']
            remark = request.POST['remark']
            client_obj = client.objects.get(pk=client_key)

            ClientCompanyList.objects.create(CompantName=CompantName, ClientName=ClientName, PhoneNo=PhoneNo,
                                             email=email,
                                             city=city, certificate=certificate, body=body, rate=rate,
                                             issueDate=issueDate,
                                             expiryDate=expiryDate if expiryDate else None, expiryYear=expiryYear,
                                             remark=remark,
                                             client_key=client_obj)

            return redirect('ConsultantClientList')

        return render(request, 'addConsultantClient.html',
                      {'companyList': companyList, 'certificateList': certificateList,
                       'statusList': statusList})
    else:
        return render(request, 'login.html')


def editConsulClient(request, id):
    if 'email' and 'id' in request.session:
        client_key = request.session['id']
        editConsulClient = ClientCompanyList.objects.get(id=id)
        companyList = CompanyList.objects.filter(client_key=client.objects.get(pk=client_key))
        certificateList = CertificateList.objects.filter(client_key=client.objects.get(pk=client_key))
        statusList = StatusList.objects.filter(client_key=client.objects.get(pk=client_key))
        if request.method == 'POST':
            CompantName = request.POST['CompantName']
            ClientName = request.POST['ClientName']
            PhoneNo = request.POST['PhoneNo']
            email = request.POST['email']
            city = request.POST['city']
            certificate = request.POST['certificate']
            body = request.POST['body']
            rate = request.POST['rate']
            issueDate = request.POST['issueDate']
            expiryDate = request.POST['expiryDate']
            expiryYear = request.POST['expiryYear']
            remark = request.POST['remark']
            status = request.POST['status']

            editConsulClient.CompantName = CompantName
            editConsulClient.ClientName = ClientName
            editConsulClient.PhoneNo = PhoneNo
            editConsulClient.email = email
            editConsulClient.city = city
            editConsulClient.certificate = certificate
            editConsulClient.body = body
            editConsulClient.rate = rate
            editConsulClient.issueDate = issueDate
            editConsulClient.expiryDate = expiryDate
            editConsulClient.expiryYear = expiryYear
            editConsulClient.remark = remark
            editConsulClient.status = status
            editConsulClient.save()

            return redirect('ConsultantClientList')

        return render(request, 'editConsulClient.html',
                      {'editConsulClient': editConsulClient, 'companyList': companyList,
                       'certificateList': certificateList,
                       'statusList': statusList
                       })
    else:
        return render(request, 'login.html')


def delConsulClient(request, id):
    delConsulClient = ClientCompanyList.objects.get(id=id)
    delConsulClient.delete()
    return redirect('ConsultantClientList')


def simple_uploadConsultantClient(request):
    if 'email' and 'id' in request.session:
        client_key = request.session['id']

        if request.method == 'POST':
            emp_resource = ConsultantClientResource()
            dataset = Dataset()
            new_income = request.FILES['myfile']

            imported_data = dataset.load(new_income.read(), format='xlsx')

            data_range = 0
            for data_col in imported_data['email']:
                if data_col is None:
                    break
                else:
                    data_range += 1

            data = imported_data
            client_obj = client.objects.get(pk=client_key)
            excelValue = []

            for data_obj in range(data_range):
                value = ClientCompanyList.objects.create(
                    client_key=client_obj,
                    CompantName=data[data_obj][0],
                    ClientName=data[data_obj][1],
                    PhoneNo=data[data_obj][2],
                    email=data[data_obj][3],
                    city=data[data_obj][4],
                    certificate=data[data_obj][5],
                    body=data[data_obj][6],
                    rate=data[data_obj][7],
                    issueDate=data[data_obj][8],
                    expiryDate=data[data_obj][9],
                    expiryYear=data[data_obj][10],
                    remark=data[data_obj][11]
                )

                excelValue.append(value)

            for valueUpdate in excelValue:
                print("--------------date ", valueUpdate.CompantName)
                print("-------------- list", valueUpdate.ClientName)

                if CompanyList.objects.filter(name__icontains=valueUpdate.CompantName,
                                              client_key=client_obj):
                    print("record found")
                else:
                    print("record not found")
                    checkCompany = CompanyList.objects.create(name=valueUpdate.CompantName,
                                                              client_key=client_obj)

                if CertificateList.objects.filter(certificateName__icontains=valueUpdate.certificate,
                                                  client_key=client_obj):
                    print("record found")
                else:
                    print("record not found")
                    checkCompany = CertificateList.objects.create(certificateName=valueUpdate.certificate,
                                                                  client_key=client_obj)

                if StatusList.objects.filter(statusList__icontains=valueUpdate.status,
                                             client_key=client_obj):
                    print("record found")
                else:
                    print("record not found")
                    checkCompany = StatusList.objects.create(statusList=valueUpdate.status,
                                                             client_key=client_obj)

                valueUpdate.save()
            value.save()

        return redirect('ConsultantClientList')


def export_csv(request):
    if 'email' and 'id' in request.session:
        client_key = request.session['id']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=ClientCompanyList' + str(datetime.now()) + '.csv'

        writer = csv.writer(response)
        writer.writerow(['CompantName', 'ClientName', 'PhoneNo', 'email', 'city', 'certificate',
                         'body', 'rate', 'issueDate', 'expiryDate',
                         'expiryYear',
                         'remark', 'status'])

        valuestore = ClientCompanyList.objects.filter(client_key=client.objects.get(pk=client_key))

        for exp in valuestore:
            writer.writerow([exp.CompantName, exp.ClientName, exp.PhoneNo, exp.email, exp.city,
                             exp.certificate,
                             exp.body, exp.rate, exp.issueDate, exp.expiryDate,
                             exp.expiryYear, exp.remark, exp.status])

        return response


def upload(request):
    return render(request, 'upload.html')


def my_scheduleMail(request):
    consultantClient = ClientCompanyList.objects.all()
    for cc in consultantClient:
        expDate = cc.expiryDate
        print("expriy date ----", expDate)
        today = date.today()
        expList = [30, 25, 20, 15, 10, 5, 2, 1]
        for exp in expList:
            expDateMonth = expDate - timedelta(days=exp)
            print(expDateMonth)
            email = cc.email
            companyName = cc.CompantName
            if expDateMonth == today:
                cc.status = "Pending"
                cc.save()
                print("Expried Soon .....", exp)
                sendmail("Expried Soon... ", "Expirymail_template", email,
                         {'exp': exp, 'companyName': companyName})
    return redirect('ConsultantClientList')


def sendmail(subject, template, to, context, lookup_kwargs=None):
    email_user = AppData.objects.get(key="EMAIL_HOST_USER")

    template_str = template + '.html'
    html_message = render_to_string(template_str, {'data': context})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, email_user, [to], html_message=html_message)


def userSetting(request):
    if 'email' and 'id' in request.session:
        client_key = request.session['id']
        print(client_key)
        notiList = NotifactionSetting.objects.get(client_key=client.objects.get(pk=client_key))
        print(notiList)
        if request.method == "POST":
            if 'emailService' in request.POST:
                emailService = request.POST['emailService']
                emailService = True
            else:
                emailService = False
            if 'smsService' in request.POST:
                smsService = request.POST['smsService']
                smsService = True
            else:
                smsService = False
            if 'fcmService' in request.POST:
                fcmService = request.POST['fcmService']
                fcmService = True
            else:
                fcmService = False
            if 'voiceNotiService' in request.POST:
                voiceNotiService = request.POST['voiceNotiService']
                voiceNotiService = True
            else:
                voiceNotiService = False

            notiList.emailService = emailService
            notiList.smsService = smsService
            notiList.fcmService = fcmService
            notiList.voiceNotiService = voiceNotiService
            notiList.save()


        return render(request, 'userSetting.html',{'notiList':notiList})
    else:
        return render(request, 'login.html')


def OTP_generator(mobNum):
    otp = randint(10000, 99999)
    list_of_otp = AndroidSetting.objects.filter(OTP=otp)
    while otp in list_of_otp:
        otp = randint(10000, 99999)
    url = "http://quicksms.highspeedsms.com/sendsms/sendsms.php?username=BREbonrix&password=sales55&type=TEXT&sender=BONRIX&mobile={0}&message=Your%20OTP%20for%20login%20verification%20is%20:=%20{1}".format(
        mobNum, otp)
    print(url)
    requests.get(url)
    return otp


@csrf_exempt
def generateOTP(request):
    if request.method == 'POST':
        mobile_num = request.POST['mobileNumber']
        otp = OTP_generator(mobile_num)
        data = {"mobileNumber": mobile_num, "OTP": otp}
        signIn.objects.create(mobileNumber=mobile_num, OTP=otp)
        response = {"status": True, "statusMsg": "SUCCESS"}
        print(otp)
        return JsonResponse(response)


@csrf_exempt
def authentication(request):
    my_data = {"mobileNumber": request.POST['mobileNumber'], "OTP": request.POST['OTP'],
               "imei": request.POST['IMEI'], "fcmtocken": request.POST["fcmTocken"], }
    print(my_data)

    allImei = AndroidSetting.objects.all().values('imei')
    print(allImei)
    allMNo = AndroidSetting.objects.all().values('mobileNumber')
    if my_data["imei"] and my_data["fcmtocken"]:
        imei_list = [x['imei'] for x in allImei]
        num_list = [x['mobileNumber'] for x in allMNo]
        my_data = my_data
        print("---------", my_data)

        if my_data["mobileNumber"] in num_list and my_data["mobileNumber"] not in imei_list:
            data = AndroidSetting.objects.get(mobileNumber=my_data["mobileNumber"]).delete()
            AndroidSetting.objects.create(mobileNumber=my_data["mobileNumber"], OTP=my_data['OTP'],
                                          imei=my_data["imei"], fcmtocken=my_data['fcmtocken'])
            response = {"status": True, "statusMsg": "SUCCESS"}
            return JsonResponse(response)

    if my_data["mobileNumber"] not in num_list and my_data["mobileNumber"] not in imei_list:
        AndroidSetting.objects.create(mobileNumber=my_data["mobileNumber"], OTP=my_data['OTP'],
                                      imei=my_data["imei"], fcmtocken=my_data['fcmtocken'])
        response = {"status": True, "statusMsg": "SUCCESS"}
        return JsonResponse(response)

    if my_data['imei'] in imei_list and my_data['mobileNumber'] not in num_list:
        data = AndroidSetting.objects.get(imei=my_data["imei"])
        data.mobileNumber = my_data['mobileNumber']
        data.save()
        response = {"status": True, "statusMsg": "SUCCESS"}
        return JsonResponse(response)


@csrf_exempt
def signup(request):
    mobile_num = request.POST['mobileNumber']
    otp = request.POST['OTP']
    user = AndroidSetting.objects.get(mobileNumber=mobile_num)
    if user:
        if user.OTP == otp:
            response = {"status": True, "statusMsg": "Success"}
            return JsonResponse(response)

    return JsonResponse({"status": False, "statusMsg": "FAIL"})


def send_message(request, mobileNumber):
    cameraName = AndroidSetting.objects.get(mobileNumber=mobileNumber)
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']

        if cameraName.phoneType == 'Android':
            print(cameraName)
            serverToken = "AAAAw1Yztd4:APA91bHZiDFpgma8K849b2FPrxukpHo7BO97v3BqtJFpVe" \
                          "-LXp9AE763yBvGEchEHic34AwqrMRMCsGx3rJAd1ecP7UYE3yaumF-BoPhO7klG6L3Z_HceCsC5CaN5HbKBqGrHA7nAu28"

            registration_id = cameraName.fcmtocken
            print(registration_id)

            push_service = FCMNotification(api_key=serverToken)

            data = {
                'title': urllib.parse.quote_plus(title),
                'message': urllib.parse.quote_plus(message),
                'timestamp': time.time(),
                'popup': False,
                'tag': urllib.parse.quote_plus("Empty"),
                'img': urllib.parse.quote_plus("Empty")
            }
            print(data)
            result = push_service.single_device_data_message(registration_id=registration_id, data_message=data)
            print(result)

            return JsonResponse(data)

        if cameraName.phoneType == 'Iphone':
            print(cameraName)
            serverToken = "AIzaSyDOBwu_SJjv9dIwr5UkSgv6WmkW-FWYYCg"

            registration_id = cameraName.fcmtocken
            print(registration_id)

            push_service = FCMNotification(api_key=serverToken)

            now = datetime.now()
            current_time = now.strftime("%d/%m/%Y %H:%M:%S")

            mainData  = {
                'to' : urllib.parse.quote_plus(registration_id),
                'content_available': urllib.parse.quote_plus('true'),
                'notification' : {
                    'alert':urllib.parse.quote_plus(''),
                    'title':urllib.parse.quote_plus('TestInfo'),
                    'sound':urllib.parse.quote_plus('default')
                },
                'data' : {
                    'title': urllib.parse.quote_plus(title),
                    'message': urllib.parse.quote_plus(message),
                    'tag': urllib.parse.quote_plus("Admin"),
                    'timestamp': urllib.parse.quote_plus("12:24:36"),
                    'popup': urllib.parse.quote_plus("false"),
                    'img': urllib.parse.quote_plus("NA")
                },
                'timestamp': current_time,
                'payload': {

                },
                "priority": 100
            }
            print(mainData)

            result = push_service.single_device_data_message(registration_id=registration_id, data_message=mainData)
            print(result)

            return JsonResponse(mainData)

        return redirect('login')

def fatchFCM(request):
    if 'email' and 'PhoneNo' in request.session:
        client_key = request.session['PhoneNo']
        print(client_key)
        FcmData = AndroidSetting.objects.filter(mobileNumber=client_key)
        url_path = AppData.objects.filter(key__icontains="FatchFCM")
        if FcmData:
            return render(request,'fatchFCM.html',{'FcmData':FcmData})
        else:
            url = url_path.get(key__icontains="FatchFCM")
            final_url = url.value.format(client_key=client_key)
            requests.get(final_url)
            AndroidSetting.objects.create(mobileNumber=client_key,phoneType='Iphone')
            return render(request, 'fatchFCM.html', {'FcmData': FcmData})
    else:
        return render(request,'login.html')


def addIphoneUser(request, id):
    FCMUser = AndroidSetting.objects.get(id=id)
    if request.method == 'POST':
        fcm = request.POST['fcm']
        FCMUser.fcmtocken = fcm
        FCMUser.save()
        return redirect('fatchFCM')
    return render(request, 'addIphoneUser.html',{'FCMUser':FCMUser})


def sendFCMUser(requset,id):
    FCMUser = AndroidSetting.objects.get(id=id)
    return render(requset,'sendFCMUser.html',{'FCMUser':FCMUser})

