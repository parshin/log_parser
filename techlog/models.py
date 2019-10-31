from django.db import models


class EXCP(models.Model):
    DateUpload = models.DateField(auto_now=True)
    Date = models.DateField(auto_now=True)
    Name = models.CharField(max_length=10, default='')
    Level = models.IntegerField(null=True)
    Process = models.CharField(max_length=20, default='')
    ProcessName = models.CharField(max_length=20, default='')
    OSThread = models.IntegerField(null=True)
    ClientID = models.IntegerField(null=True)
    ApplicationName = models.CharField(max_length=20, default='')
    ComputerName = models.CharField(max_length=20, default='')
    ConnectID = models.IntegerField(null=True)
    SessionID = models.IntegerField(null=True)
    User = models.CharField(max_length=200, default='')
    AppID = models.CharField(max_length=20, default='')
    Exception = models.CharField(max_length=36, default='')
    Description = models.CharField(max_length=200, default='')
    Context = models.CharField(max_length=300, default='')


