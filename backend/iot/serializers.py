from rest_framework import serializers
from .models import City
from .models import Device, Event
from .models import Resident

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'