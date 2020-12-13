from django.test import TestCase
from .models import Account, City, Role 
from .models import Resident, Visitor
from .models import StreetSign, Status, InformationKiosk
from .models import Camera, CameraEvent, Microphone, MicrophoneEvent, Thermometer, ThermometerEvent, CO2Meter, CO2Event

# Create your tests here.
class CityTestCase(TestCase):
    def setUp(self):
        City.objects.create(name= 'Rio de Janeiro', account = Account.objects.create())
        City.objects.create(name= 'New York', account = Account.objects.create())

    def test_city_accounts(self):
        city_rio = City.objects.get(name='Rio de Janeiro')
        city_ny = City.objects.get(name='New York')
        print(city_rio.account)
        print(city_ny.account)

        account_1 = Account.objects.get(pk=1)
        print("Account 1 city ", account_1.city)

class PeopleTestCase(TestCase):
    def setUp(self):
        adult_role = Role.objects.create(name = "adult_role")
        Resident.objects.create(account = Account.objects.create(), name = "John" ,phone = "21-3333-4444", role=adult_role)
        Resident.objects.create(account = Account.objects.create(), name = "Mary" ,phone = "21-3332-4242", role=adult_role)
        Visitor.objects.create()

    def test_read_people(self):
        resident_1 = Resident.objects.get(name="John")
        visitors  = Visitor.objects.all()

        print(resident_1)
        print('visitors = ', visitors)

        adult_role = Role.objects.get(pk=1)
        print("Role ", adult_role)
        print("Role resident", adult_role.resident_set.all())

    def test_update_people(self):
        resident_1 = Resident.objects.get(name="John")
        print('Resident info = ',resident_1)
        
        resident_1.latitude = 123
        resident_1.save()
        del resident_1

        resident_1new = Resident.objects.get(name="John")
        print('Resident info = ',resident_1new)

        self.assertEqual(resident_1new.latitude, 123)


class DeviceTestCase(TestCase):
    def setUp(self):
        city_dubai = City.objects.create(name="Dubai", account = Account.objects.create())
        StreetSign.objects.create(account = Account.objects.create(), status=Status.WORKING, enabled = True, city=city_dubai, text = "Speed Limit 50")

    def test_streetSign(self):
        street_sign = StreetSign.objects.get(pk=1)
    
        print(street_sign)
        print('updating status .... ')

        street_sign.status = Status.UNDER_MAINTENANCE
        street_sign.save()
        del street_sign

        street_sign_new = StreetSign.objects.get(pk=1)
        print(street_sign_new)

        self.assertEqual(Status(street_sign_new.status), Status.UNDER_MAINTENANCE)

        print("See the location of the sign")
        print("Street Sign city ", street_sign_new.city)


class SensorTestCase(TestCase):
    def setUp(self):
        city_dubai = City.objects.create(name="Dubai", account = Account.objects.create())
        
        

        device_infoKiosk = InformationKiosk(account = Account.objects.create(), status=Status.WORKING, 
        enabled = True, city=city_dubai)
        device_infoKiosk.save()

        mic = Microphone.objects.create(device = device_infoKiosk)
        mic.save()
        camera = Camera.objects.create(device = device_infoKiosk)
        camera.save()
        thermometer = Thermometer.objects.create(device = device_infoKiosk)
        thermometer.save()
        co2Meter = CO2Meter.objects.create(device = device_infoKiosk)
        co2Meter.save()

    def test_streetSign(self):
        info_kiosk = InformationKiosk.objects.get(pk=1)
        print(info_kiosk)
        print('Info Kiosk sensors...')
        sensors = info_kiosk.inputsensor_set.all()
        print(sensors)

        print('Info Kiosk microfone...')
        print(Microphone.objects.filter(device=info_kiosk)[0])
        
        

