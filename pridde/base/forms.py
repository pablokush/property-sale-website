from dataclasses import fields
import imp
from pyexpat import model
from statistics import mode
from django.forms import ModelForm
from .models import ClientMessages, CompanyDetails, Location, Owners, Property, PropertyImage


class PropertyForm(ModelForm):
    class Meta:
        model=Property
        fields='__all__'


class OwnerForm(ModelForm):
    class Meta:
        model=Owners
        fields='__all__'

class CompanyDetailsForm(ModelForm):
    class Meta:
        model=CompanyDetails
        fields='__all__'


class CommentForm(ModelForm):
    class Meta:
        model=ClientMessages
        fields='__all__'


class PropertyImages(ModelForm):
    class Meta:
        model=PropertyImage
        fields='__all__'

class LocationForm(ModelForm):
    class Meta:

        model=Location
        fields='__all__'

class ImagesForm(ModelForm):
    class Meta:
        model=PropertyImage
        fields='__all__'