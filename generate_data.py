# python manage.py shell < generate_data.py

from iot.models import Account, City 
from iot.models import Role, Resident, Visitor
from iot.models import StreetSign, Status, InformationKiosk
from iot.models import Camera, CameraEvent, Microphone, MicrophoneEvent, Thermometer, ThermometerEvent, CO2Meter, CO2Event, InputSensor


City.objects.create(name= 'Rio de Janeiro', account = Account.objects.create())
City.objects.create(name= 'New York', account = Account.objects.create())

adult_role = Role.objects.create(name = "adult_role")
Resident.objects.create(account = Account.objects.create(), name = "John" ,phone = "21-3333-4444", role=adult_role)
Resident.objects.create(account = Account.objects.create(), name = "Mary" ,phone = "21-3332-4242", role=adult_role)
Visitor.objects.create()

city_dubai = City.objects.create(name="Dubai", account = Account.objects.create())

device_infoKiosk = InformationKiosk(account = Account.objects.create(), status=Status.WORKING, 
enabled = True, city=city_dubai)
device_infoKiosk.save()

Camera.objects.create(device = device_infoKiosk)
Microphone.objects.create(device = device_infoKiosk)
Thermometer.objects.create(device = device_infoKiosk)
CO2Meter.objects.create(device = device_infoKiosk)


