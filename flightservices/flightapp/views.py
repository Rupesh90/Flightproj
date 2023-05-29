from django.shortcuts import render
from flightapp.models import Flight,Passenger,Resrvation
from rest_framework import viewsets
from flightapp.serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
@api_view(['POST'])
def Find_flights(request):
    flights=Flight.objects.filter(departureCity=request.data['departureCity'],arrivalCity=request.data['arrivalCity'],dateofDeparture=request.data['dateofDeparture'])
    serializer=FlightSerializer(flights,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def save_reservation(request):
    flight=Flight.objects.get(id=request.data['flightId'])
    passenger=Passenger()
    passenger.firstname=request.data['firstname']
    passenger.lastname=request.data['lastname']
    passenger.middlename=request.data['middlename']
    passenger.email=request.data['email']
    passenger.phone=request.data['phone']
    passenger.save()

    reservation=Resrvation()
    reservation.flight=flight
    reservation.passenger=passenger
    reservation.save()
    return Response(status=status.HTTP_201_CREATED)

     

class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
     queryset=Passenger.objects.all()
     serializer_class=PassengerSerializer 

class ReservationViewSet(viewsets.ModelViewSet):
     queryset=Resrvation.objects.all()
     serializer_class=ReservationSerializer

