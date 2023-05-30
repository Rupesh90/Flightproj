from flightapp.models import Flight,Passenger,Resrvation
from rest_framework import serializers
import re

#this below validator used less 
def isFlightNumberValid(flightNumber):
    print(data)
    print("IsFlightnumbervalid")

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'
        validators=[isFlightNumberValid]

    def validate_flightNumber(self,flightNumber):
         if(re.match("^[a-zA-Z0-9]*$",flightNumber)==None):
             raise serializers.ValidationError("Invalid number Make sure it is alpha numeric")
         return flightNumber    

    def validate(self,date):
        print("validate")
        print(data['flightNumber'])
        return data

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resrvation
        fields='__all__'