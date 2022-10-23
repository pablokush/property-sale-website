from django.db import models

# Create your models here.
from ast import mod
from ctypes import addressof
import email
from django.db import models
from django.forms import ImageField

# Create your models here.

class Client(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    companyname=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.email
class Owners(models.Model):
   
    email=models.EmailField()
    phone1=models.CharField(max_length=15)
    phone2=models.CharField(max_length=15,blank=True)
    companyname=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.companyname


class Location(models.Model):
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.location

class Property(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    description=models.TextField()
    location=models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to="images")
    area=models.DecimalField(max_digits=9,decimal_places=2)
    bedroom=models.IntegerField()
    bathrooms=models.IntegerField()
    Use=models.TextChoices("Use","Rent Sell")
    usage=models.CharField(max_length=100,blank=False,choices=Use.choices)
    owner=models.ForeignKey(Owners,on_delete=models.SET_NULL,null=True)
    amenities=models.TextField(blank=True)
    # comments=models.ForeignKey(ClientMessages,on_delete=models.DO_NOTHING,blank=True)
    features=models.TextField(blank=True)
    def __str__(self):
        return self.name

    def set_list(self,element):
        self.features += "." + element if self.features else element

    def get_list(self):
        return self.features.split(".") if self.features else None

    def set_list(self,element):
        self.amenities += "." + element if self.amenities else element

    def get_list(self):
        return self.amenities.split(".") if self.amenities else None




class ClientMessages(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    comments=models.TextField(max_length=500)
    property=models.ForeignKey(Property,on_delete=models.SET_NULL,null=True)
    

    def __str__(self):
        return self.comments


class CompanyDetails(models.Model):
    name=models.CharField(max_length=100)
    phone1=models.CharField(max_length=20)
    phome2=models.CharField(max_length=20)
    description=models.TextField(max_length=300)
    email1=models.EmailField()
    email2=models.EmailField()
    address=models.TextField(max_length=200)
    clients=models.CharField(max_length=10)
    rented=models.CharField(max_length=10)
    sales=models.CharField(max_length=15)
    sellingDescription=models.TextField(max_length=300)
    leasingDescription=models.TextField(max_length=300)
    advertisingDescription=models.TextField(max_length=300)
    def __str__(self):
        return self.name


class PropertyImage(models.Model):
    image=models.ImageField(upload_to="images")
    property=models.ForeignKey(Property,default=None,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.property.name