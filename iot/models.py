from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

# Create your models here.
class Account(models.Model):
    def __str__(self):
        return " account id " + str(self.id)

class City(models.Model):
    name = models.CharField(max_length=200)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, editable=False)
    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)
    radius = models.FloatField(default = 0.0)

    def __str__(self):
        return self.name + " with account " + self.account.__str__() + " at lat " + str(self.latitude) + " and long " + str(self.longitude) + " with radius "+ str(self.radius)

# ------ People --------

class Role(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return "Role " + self.name

class Person(models.Model):
    # ABSTRACT CLASS - SHOULDN'T BE INSTANTIATED
    latitude = models.IntegerField(default = 0)
    longitude = models.IntegerField(default = 0)
    
    def __str__(self):
        return "Person at lat " + str(self.latitude) + " and long " + str(self.longitude)

class Resident(Person):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, editable = False)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12,null=True, validators=[RegexValidator(r'^\d{2}-\d{4}-\d{4}$')])
    role = models.ForeignKey(Role, on_delete = models.CASCADE)
    
    def __str__(self):
        return "Resident with id "+ str(self.id) + " name " + self.name + " with account " + self.account.__str__() + " at lat " + str(self.latitude) + " and long " + str(self.longitude)

class Visitor(Person):
    
    def __str__(self):
        return "Visitor with id " + str(self.id) + " at lat " + str(self.latitude) + " and long " + str(self.longitude)

# ------ Devices --------
class Status(models.TextChoices):
    WORKING = 'W', 'Working'
    NOT_WORKING = 'NW', 'Not Working'
    UNDER_MAINTENANCE = 'UM', 'Under Maintenance'

class Device(models.Model):
    # ABSTRACT CLASS - SHOULDN'T BE INSTANTIATED
    account = models.OneToOneField(Account, on_delete=models.CASCADE, editable = False)
    latitude = models.FloatField(default = 0)
    longitude = models.FloatField(default = 0)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.WORKING)
    enabled = models.BooleanField()
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return "Device id " + str(self.id) + " with account " + self.account.__str__() + " at lat " + str(self.latitude) + " and long " + str(self.longitude) + " with status "+ Status(self.status).label + " enabled " + str(self.enabled)

class StreetSign(Device):
    text = models.CharField(max_length= 200)

    def __str__(self):
        return "Street Sign device with properties" + super().__str__()

'''
# ------ Input sensors --------
class InputSensor(models.Model):
    # ABSTRACT CLASS - SHOULDN'T BE INSTANTIATED
    device = models.ForeignKey('Device', on_delete = models.CASCADE)

class Event(models.Model):
    creation_date = models.DateTimeField('date created', null=True)
    finish_date = models.DateTimeField('date finalized', null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True)
    InputSensor = models.ForeignKey(InputSensor, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return " event created at " + str(self.creation_date) + " and finalized at " + str(self.finish_date)

class Microfone(InputSensor):
    def __str__(self):
        return " microfone at device " + str(self.device.str())

class Thermometer(InputSensor):
    def __str__(self):
        return " thermometer at device " + str(self.device.str())

class CO2Meter(InputSensor):
    def __str__(self):
        return " co2 meter at device " + str(self.device.str())

class Camera(InputSensor):
    def __str__(self):
        return " camera at device " + str(self.device.str())

'''