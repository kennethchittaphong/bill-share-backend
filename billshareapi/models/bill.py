from django.db import models
from .user import User
class Bill(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    due_date = models.DateField(max_length=55)
    total_amount = models.IntegerField(null=True)
    split_amount = models.JSONField()
    status = models.CharField(max_length=55)

    def __str__(self):
        return self.name