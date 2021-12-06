from django.shortcuts import render
from flightApp.models import Flight,Passeger,Reservation
from flightApp.serializers import FLightSerializer,PassegerSerializer,ReservationSerializer
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
def find_flights(request):
    flights=Flight.objects.filter(departureCity=request.data['departtureCity'],arrivalCity=request.data['arrivalCity'],dateOfDeparture=request.data['dateOfDeparture'])
    serializer=FLightSerializer(flights,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def save_reservation(request):  
    flight = Flight.objects.get(id=request.data['flightId'])  
    passeger = Passeger()
    passeger.firstName = request.data['firstName']
    passeger.lastName = request.data['lastName']
    passeger.middleName = request.data['middleName']
    passeger.email = request.data['email']
    passeger.phone = request.data['phone']
    passeger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passeger = passeger

    reservation.save()
    return Response(status=status.HTTP_201_CREATED)


class FlightViewSets(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FLightSerializer
    permission_classes=(IsAuthenticated,)

class PassegerViewSets(viewsets.ModelViewSet):
    queryset=Passeger.objects.all()
    serializer_class=PassegerSerializer    

class ReservationViewSets(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer