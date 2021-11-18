from django.db import models

# Create your models here.
class Package(models.Model):
    Sno=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to="package/")
    location=models.CharField(max_length=100,default="")
    price=models.IntegerField(default=0)
    duration=models.CharField(max_length=200, default="")
    famous=models.CharField(max_length=500, default="")
    payopt=models.CharField(max_length=100, default="")
    hotel1=models.CharField(max_length=100, default="")
    hotel2=models.CharField(max_length=100, default="")
    hotel3=models.CharField(max_length=100, default="")
    hotelimage1=models.ImageField(upload_to="hotelimage/")
    hotelimage2=models.ImageField(upload_to="hotelimage/")
    hotelimage3=models.ImageField(upload_to="hotelimage/")
    contentimage1=models.ImageField(upload_to="contentimage/")
    contentimage2=models.ImageField(upload_to="contentimage/")
    contentimage3=models.ImageField(upload_to="contentimage/")
    content1=models.CharField(max_length=500, default="")
    content2=models.CharField(max_length=500, default="")
    content3=models.CharField(max_length=500, default="")
    content=models.TextField()
    slug=models.CharField(max_length=100 , default="")

    def __str__(self):
        return self.location

class Hotel(models.Model):
    Sr=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to='hotel/')
    name=models.CharField(max_length=200, default="")
    place=models.CharField(max_length=500, default="")
    availability=models.CharField(max_length=100, default="")
    rating=models.IntegerField(default=0)
    contact=models.CharField(max_length=100, default=0)

    def __str__(self):
        return self.name
