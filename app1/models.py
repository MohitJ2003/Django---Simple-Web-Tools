from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Users():
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)



class Transaction(models.Model):
    date = models.DateField()
    time = models.TimeField()
    transaction_details = models.CharField(max_length=255)
    your_account = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    upi_ref_no = models.CharField(max_length=50, blank=True, null=True)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return f"{self.date} - {self.transaction_details} - {self.amount}"
