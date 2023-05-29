from flightapp.models import Flight,Passenger,Resrvation
from rest_framework import serializers


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resrvation
        fields='__all__'