from django.db import models

# Create your models here.

class Vetclinics(models.Model):
    name = models.CharField(max_length= 50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)


    def __str__(self):
        return self.name

