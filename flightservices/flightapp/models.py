from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token #this is model(exist in DRF(django rest framw...))
from django.conf import settings
# Create your models here.
class Flight(models.Model):
    flightnumber=models.CharField(max_length=20)
    operatingAirlines=models.CharField(max_length=20)
    departureCity=models.CharField(max_length=20)
    arrivalCity=models.CharField(max_length=20)
    dateofDeparture=models.DateField()
    esitmatedTimeOfDeparture=models.TimeField()


class Passenger(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    middlename=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)   

class Resrvation(models.Model):
    #flight=models.OnetoOne(Flight,on_delete=models.CASCADE)
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger=models.ForeignKey(Passenger,on_delete=models.CASCADE)    

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_authtokens(sender,instance,created,**kwargs):
    if created:
         Token.objects.create(user=instance)  #we have User in admin
