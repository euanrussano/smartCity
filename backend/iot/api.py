# contact/api.py
from rest_framework import viewsets
from .serializers import CitySerializer, DeviceSerializer, ResidentSerializer
from .models import City
from .models import Device
from .models import Resident


class CityViewSet(viewsets.ModelViewSet):
   serializer_class = CitySerializer
   queryset = City.objects.all()

class DeviceViewSet(viewsets.ModelViewSet):
   serializer_class = DeviceSerializer
   queryset = Device.objects.all()

class ResidentViewSet(viewsets.ModelViewSet):
   serializer_class = ResidentSerializer
   queryset = Resident.objects.all()