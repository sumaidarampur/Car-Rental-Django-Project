from django.db import models
from django.contrib.auth.models import User

class SignUp(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    e_mail = models.EmailField(max_length= 40)
    password = models.CharField(max_length= 50)


class Contact(models.Model):
    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length= 20)
    e_mail = models.EmailField(max_length= 200)
    phone_number = models.IntegerField()
    contact_message=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)