from django.db import models
from .user import User

class People(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    due_date = models.DateField(max_length=55)
    amount = models.IntegerField(null=True)
    status = models.CharField(max_length=55)
    bill_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name