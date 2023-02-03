from django.db import models
from .bill import Bill

class People(models.Model):
    
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=55)
    due_date = models.DateField(max_length=55)
    amount = models.IntegerField(null=True)
    status = models.CharField(max_length=55)

    def __str__(self):
        return self.name