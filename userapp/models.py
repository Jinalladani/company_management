from idlelib.mainmenu import default_keydefs

from django.db import models


# Create your models here.
class client(models.Model):
    username = models.CharField(max_length=128, null=True, blank=True)
    PhoneNo = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    otp = models.CharField(max_length=6, default=359)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)


class ClientCompanyList(models.Model):
    client_key = models.ForeignKey(client, on_delete=models.CASCADE, null=True)
    CompantName = models.CharField(max_length=256, null=True, blank=True)
    ClientName = models.CharField(max_length=256, null=True, blank=True)
    PhoneNo = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    certificate = models.CharField(max_length=128, null=True, blank=True)
    body = models.CharField(max_length=512, null=True, blank=True)
    rate = models.CharField(max_length=128, null=True, blank=True)
    issueDate = models.DateField(null=True, blank=True)
    expiryDate = models.DateField(null=True, blank=True)
    expiryYear = models.CharField(max_length=128, null=True, blank=True)
    remark = models.CharField(max_length=128, null=True, blank=True)
    status = models.CharField(max_length=128, default='Renew', null=True, blank=True)


class CompanyList(models.Model):
    client_key = models.ForeignKey(client, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=128, null=True, blank=True)


class CertificateList(models.Model):
    client_key = models.ForeignKey(client, on_delete=models.CASCADE, null=True)
    certificateName = models.CharField(max_length=128, null=True, blank=True)


class StatusList(models.Model):
    client_key = models.ForeignKey(client, on_delete=models.CASCADE, null=True)
    statusList = models.CharField(max_length=128, null=True, blank=True)


class AppData(models.Model):
    key = models.CharField(max_length=1000)
    value = models.TextField()

    def __str__(self):
        return str(self.key)


class signIn(models.Model):
    mobileNumber = models.CharField(max_length=10, null=True, blank=True)
    OTP = models.CharField(max_length=6, default=963852, null=True, blank=True)


class AndroidSetting(models.Model):
    mobileNumber = models.CharField(max_length=10, null=True, blank=True)
    OTP = models.CharField(max_length=6, default=963852, null=True, blank=True)
    imei = models.CharField(max_length=512, null=True, blank=True)
    fcmtocken = models.CharField(max_length=512, null=True, blank=True)
    phoneType = models.CharField(max_length=128, default='Android', null=True, blank=True)


class NotifactionSetting(models.Model):
    client_key = models.ForeignKey(client, on_delete=models.CASCADE, null=True)
    emailService = models.BooleanField(default=False,null=True, blank=True)
    smsService = models.BooleanField(default=False,null=True, blank=True)
    fcmService = models.BooleanField(default=False,null=True, blank=True)
    voiceNotiService = models.BooleanField(default=False,null=True, blank=True)
    defaultTime = models.TimeField(null=True, blank=True)


