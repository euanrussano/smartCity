from django.db import models

# Create your models here.
class Account(models.Model):
    def __str__(self):
        return " account id " + str(self.id)
