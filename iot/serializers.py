from rest_framework import serializers
from .models import City
from .models import Device
from .models import Resident


class CitySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="iot:city_detail")
    
    class Meta:
        model = City
        fields = '__all__'
        

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="iot:device_detail")
    city_holder = CitySerializer()
    class Meta:
        model = Device
        fields = '__all__'
        

class ResidentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="iot:resident_detail")
    class Meta:
        model = Resident
        fields = ['name', 'phone','url'] # add role