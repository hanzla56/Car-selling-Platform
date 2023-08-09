from django.db import models

# These below three lines added manually
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.

class Car_make(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name





class Car(models.Model):
    CONDITION_CHOICES = (
    ('new', 'New'),
    ('like_new', 'Like New'),
    ('excellent', 'Excellent'),
    ('good', 'Good'),
    ('fair', 'Fair'),
    ('poor', 'Poor'),
)

    TRANSMISSION_CHOICES = (
    ('automatic', 'Automatic'),
    ('manual', 'Manual'),
)

    FUEL_TYPE_CHOICES = (
    ('gasoline', 'Gasoline'),
    ('diesel', 'Diesel'),
    ('hybrid', 'Hybrid'),
    ('electric', 'Electric'),
    ('other', 'Other'),
)
    name = models.CharField(max_length=50)
    image = models.ImageField()
    car_make = models.ForeignKey(Car_make , on_delete=models.CASCADE)
    price = models.IntegerField()
    km_driven = models.FloatField()
    date = models.DateField(blank=True , null=True)
    condition = models.CharField(max_length=30 , choices=CONDITION_CHOICES)
    transmission = models.CharField(max_length=30 ,choices=TRANSMISSION_CHOICES)
    owner_name = models.CharField(max_length=50)
    owner_email = models.EmailField()
    owner_contact = models.IntegerField()


    def __str__(self):
        return self.name

