from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Appointment(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank= True)
    client_id = models.IntegerField()
    service_id = models.IntegerField()
    scheduled_date= models.DateField(default=datetime.now)
    status = models.CharField(max_length=100)

