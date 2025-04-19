from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Users():
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)


class PassbookPaymentHistory(models.Model):
    date = models.DateField(null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    account_name = models.CharField(max_length=255, null=True, blank=True)
    payment_mode = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_id} - {self.amount}"
