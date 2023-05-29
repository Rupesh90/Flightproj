from django.db import models

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
    passenger=models.OneToOneField(Passenger,on_delete=models.CASCADE)    
