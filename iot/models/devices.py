from django.db import models
from .city import  City
from .ledger import Account

# ------ Input sensors --------

class InputSensor(models.Model):
    # ABSTRACT CLASS - SHOULDN'T BE INSTANTIATED
    device = models.ForeignKey('Device', on_delete=models.CASCADE)

    def __str__(self):
        return " sensor with id " + str(self.id) + " at device " + str(self.device.__str__())

class Microphone(InputSensor):
    def __str__(self):
        return " Microphone "  + super().__str__()

class Thermometer(InputSensor):
    def __str__(self):
        return " Thermometer " + super().__str__()

class CO2Meter(InputSensor):
    def __str__(self):
        return " Co2 Meter " + super().__str__()

class Camera(InputSensor):
    def __str__(self):
        return " Camera " + super().__str__()

# ------ Output sensors --------
class OutputSensor(models.Model):
    # ABSTRACT CLASS - SHOULDN'T BE INSTANTIATED
    device = models.ForeignKey('Device', on_delete=models.CASCADE)

    def __str__(self):
        return " output sensor with id " + str(self.id) + " at device " + str(self.device.__str__())

class Speaker(OutputSensor):
    audioTranscript = models.CharField(max_length= 200)
    
    def __str__(self):
        return " Speaker audio transcript " + self.audioTranscript + super().__str__()

# ------ Devices --------

class Status(models.TextChoices):
    WORKING = 'W', 'Working'
    NOT_WORKING = 'NW', 'Not Working'
    UNDER_MAINTENANCE = 'UM', 'Under Maintenance'

class Device(models.Model):
    # ABSTRACT CLASS - SHOULDN'T BE INSTANTIATED
    account = models.OneToOneField(Account, on_delete=models.CASCADE, editable = False)
    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.WORKING)
    enabled = models.BooleanField(default=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True)
    
    def get_name(self):
        return 'Device'

    def __str__(self):
        return self.get_name() + " id " + str(self.id) + " with account " + self.account.__str__() + " at lat " + str(self.latitude) + " and long " + str(self.longitude) + " with status "+ Status(self.status).label + " enabled " + str(self.enabled)

class StreetSign(Device):
    text = models.CharField(max_length= 200)

    def get_name(self):
        return 'Street Sign'

    def __str__(self):
        return super().__str__() + " with text " + self.text

class InformationKiosk(Device):
    
    def purchase_ticket(self, person, event):
        # The Kiosk can also support purchasing tickets for concerts and other events.
        # check the event price
        # check if person has balance
        # charge person
        # emit event ticket to person
        raise NotImplementedError
    
    def get_name(self):
        return 'Information Kiosk'

    def __str__(self):
        return "Information Kiosk " + super().__str__()

class StreetLight(Device):
    brightness = models.FloatField(default=1.0)

    def get_name(self):
        return 'Street Light'

    def __str__(self):
        return "Street Light " + super().__str__()

class Robot(Device):

    def get_name(self):
        return 'Robot'

    def __str__(self):
        return "Robot " + super().__str__()

class ParkingSpace(Device):

    fee = models.FloatField(default=0.0)
    
    def get_name(self):
        return 'Parking Space'

    def charge(self, vehicle, hours):
        # A parking space has an hourly rate which is charged
        # to the account associated with the vehicle.
        raise NotImplementedError

    def __str__(self):
        return "Parking Space " + super().__str__()

class VehicleType(models.TextChoices):
    BUS = 'B', 'Bus'
    CAR = 'C', 'Car'

class Vehicle(Device):

    vehicleType = models.CharField(max_length=1, choices=VehicleType.choices, default=VehicleType.CAR)
    maximumCapacity = models.IntegerField(default=1)
    fee = models.FloatField(default=0.0)

    def get_name(self):
        return 'Vehicle'

    def charge(self, person):
        # Riding in a Bus or Car is free for Visitors, 
        # but requires a fee for Residents.
        raise NotImplementedError

    def __str__(self):
        return "Parking Space " + super().__str__()