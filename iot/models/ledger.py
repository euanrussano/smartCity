from django.db import models

# Create your models here.
class AccountHolder(models.Model):
    # Generic class to define someone who can have an account
    accountHolder_id = models.AutoField(primary_key=True)
        
class Account(models.Model):
    holder = models.OneToOneField(AccountHolder, on_delete=models.CASCADE)

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save)
def create_account(sender, instance, created, **kwargs):
    if isinstance(instance, AccountHolder) and created:
        print("here")
        Account.objects.create(holder=instance)
    


