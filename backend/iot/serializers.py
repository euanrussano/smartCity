from rest_framework import serializers
from .models import City
from .models import Device, Event
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


class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance