from django.db import models
from .bill import Bill

class Payment(models.Model):
    
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, default='')
    label = models.CharField(max_length=55)
    date_paid = models.DateField(max_length=55)
    amount_paid = models.IntegerField(null=True)
    payment_type = models.CharField(max_length=55)
    
    def __str__(self):
        return self.label