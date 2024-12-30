from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25)


class Car(models.Model):
    name=models.CharField(max_length=25)
    image=CloudinaryField('image')
