# python manage.py shell < generate_data.py

from iot.models import Account, City 
from iot.models import Role, Resident, Visitor
from iot.models import StreetSign, Status, InformationKiosk, StreetLight
from iot.models import Camera, CameraEvent, Microphone, MicrophoneEvent, Thermometer, ThermometerEvent, CO2Meter, CO2Event, InputSensor

City.objects.create(name= 'Rio de Janeiro')
City.objects.create(name= 'New York')

adult_role = Role.objects.create(name = "adult_role")
Resident.objects.create(name = "John" ,phone = "21-3333-4444", role=adult_role)
Resident.objects.create(name = "Mary" ,phone = "21-3332-4242", role=adult_role)
Visitor.objects.create()

city_dubai = City.objects.create(name="Dubai")

device_streetSign = StreetSign(status=Status.WORKING, 
enabled = True, city_holder=city_dubai, text = "Speed limit 80 km/h")
device_streetSign.save()

device_infoKiosk = InformationKiosk(status=Status.WORKING, 
enabled = True, city_holder=city_dubai)
device_infoKiosk.save()

device_streetLight = StreetLight(status=Status.WORKING, 
enabled = True, city_holder=city_dubai, brightness = 1.0)
device_streetLight.save()

Camera.objects.create(device = device_infoKiosk)
Microphone.objects.create(device = device_infoKiosk)
Thermometer.objects.create(device = device_infoKiosk)
CO2Meter.objects.create(device = device_infoKiosk)
