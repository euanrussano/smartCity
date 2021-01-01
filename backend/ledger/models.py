from django.db import models
from django.utils import timezone

class Account(models.Model):
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return 'account id ' + str(self.id) + ' with balance ' + str(self.balance)

class Transaction(models.Model):
    amount = models.FloatField(default=0.0)
    payer = models.ForeignKey(Account, on_delete = models.CASCADE, related_name='transaction_payer')
    receiver = models.ForeignKey(Account, on_delete= models.CASCADE, related_name='transaction_receiver')
    note = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def validate(self):
        if self.payer.balance < self.amount:
            return False
        return True

    def save(self, *args, **kwargs):
        if self.validate():
            self.payer.balance -= self.amount
            self.receiver.balance += self.amount

            self.payer.save()
            self.receiver.save()

            super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return 'transaction at ' + str(self.created_at) + ' amount ' + str(self.amount) + ' from ' + str(self.payer.id) + ' to ' + str(self.receiver.id) + ' note ' + self.note

'''
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save)
def create_account(sender, instance, created, **kwargs):
    if isinstance(instance, AccountHolder) and created:
        print("here")
        Account.objects.create(holder=instance)
'''