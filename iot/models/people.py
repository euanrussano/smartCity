from django.db import models
from django.core.validators import RegexValidator

from .ledger import Account

class Role(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return "Role " + self.name

class Person(models.Model):
    # ABSTRACT CLASS - SHOULDN'T BE INSTANTIATED
    latitude = models.IntegerField(default = 0)
    longitude = models.IntegerField(default = 0)
    
    class Meta:
        abstract = True

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