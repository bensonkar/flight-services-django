from rest_framework import serializers
from flightApp.models import Flight,Passeger,Reservation
import re


class FLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields='__all__'

    def validate_flightNumber(self,flightNumber):
        if (re.match("^[a-zA-z0-9]*$",flightNumber)==None):
            raise serializers.ValidationError("Invalid flight number.Make sure sure its alpha numeric")
        return flightNumber  

    def validate(self,data):
        print('validate ',data)
        return data      

class PassegerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passeger
        fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields='__all__'                