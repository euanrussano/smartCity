from django.db import models

from .ledger import Account, AccountHolder

class City(AccountHolder):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)
    radius = models.FloatField(default = 0.0)

    def __str__(self):
        return self.name + " with id " + str(self.accountHolder_id) + " with account " + self.account.__str__() + " at lat " + str(self.latitude) + " and long " + str(self.longitude) + " with radius "+ str(self.radius)