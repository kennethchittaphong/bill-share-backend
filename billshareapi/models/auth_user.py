from django.db import models


class AuthUser(models.Model):

    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    is_staff = models.CharField(max_length=50)
    is_active = models.CharField(max_length=50)
    last_login = models.DateTimeField(max_length=50)
    is_superuser = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name