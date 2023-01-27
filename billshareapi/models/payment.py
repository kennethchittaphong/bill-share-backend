from django.db import models

class Payment(models.Model):
    
    uid = models.CharField(max_length=55)
    name = models.CharField(max_length=55)
    date = models.DateField(max_length=55)
    payment_type = models.CharField(max_length=55)
    
    def __str__(self):
        return self.name