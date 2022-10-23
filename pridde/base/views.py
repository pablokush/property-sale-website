from multiprocessing import context
from pydoc import pager
from pyexpat import features
from django.shortcuts import redirect, render


from base.forms import CommentForm, CompanyDetailsForm, ImagesForm, LocationForm, OwnerForm, PropertyForm
from .models import CompanyDetails, Location, Owners, Property
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
# Create your views here.

def loginPage(request):
    page="login"

    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"User Does Not Exist")

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("custom")
        else:
            messages.warning(request,"Username or password Does not exist")
    context={
        "page":page
    }

    return render(request,"base/login-register.html",context)



def logoutUser(request):
    logout(request)
    return redirect("home")



def reigsterUser(request):
    page="register"
    context={
        "page":pager
    }
    return render(request,"base/base/login-register.html",context)



def index(request):
    q=request.GET.get("q") if request.GET.get('q') !=None else ''
    propertyItem=Property.objects.filter(
        Q(location__location__icontains=q)
    )
    count=propertyItem.count()
    details=CompanyDetails.objects.all()
    location=Location.objects.all()
    context={
        "properties":propertyItem,
         "details":details,
         "location":location,
         "count":count
    }
    return render(request,"base/index.html",context)



def details(request,pk):
    form=CommentForm()
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details')
    propertyItem=Property.objects.get(id=pk)
    features=Property.objects.filter(id=pk).values_list('features',flat=True)
    
    f_list=list(features)
    fin=list(f_list[0].split("."))
    print(fin[0])

    amenities=Property.objects.filter(id=pk).values_list('amenities',flat=True)
    amenities_set=list(amenities)
    amenities_list=list(amenities_set[0].split("."))

    imageList=propertyItem.propertyimage_set.all()
    context={
        "propertyItem":propertyItem,
        "form":form,
        "images":imageList,
        "features":fin,
        "amenities":amenities_list
        
    }
    return render(request,"base/details.html",context)


def panel(request):
    propertyItem=Property.objects.all()
    owners=Owners.objects.all()
    details=CompanyDetails.objects.all()
    count=propertyItem.count()
    context={
        "properties":propertyItem,
        "owners":owners,
        "details":details,
        'count':count
    }
    return render(request,"base/admin.html",context)


def addproperty(request):
    page="add"
    form=PropertyForm()
    if request.method == "POST":
        form=PropertyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("custom")


    context={
        "form":form,
        "page":page


    }
    return render(request,"base/add-property.html",context)
    
def editProperty(request,pk):
    propertyItem=Property.objects.get(id=pk)
    form=PropertyForm(instance=propertyItem)
    page="edit"
    if request.method == "POST":
        form=PropertyForm(request.POST,instance=propertyItem)
        if form.is_valid():
            form.save()
            return redirect("custom")

    context={
        "form":form,
        "page":page
    }

    return render(request,"base/add-property.html",context)



def deleteProperty(request,pk):
    propertyItem=Property.objects.get(id=pk)

    if request.method == "POST":
        propertyItem.delete()
        return redirect("custom")

    return render(request,"base/delete.html",{"obj":propertyItem})


def addOwner(request):
    form=OwnerForm()
    if request.method == "POST":
        form=OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("custom")


    context={
        "form":form,
       

    }
    return render(request,"base/add-owner.html",context)
    
def companyDetails(request):
    form=CompanyDetailsForm()
    if request.method == "POST":
        form=CompanyDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("custom")


    context={
        "form":form,
       

    }
    return render(request,"base/company-details.html",context)

def editCompanyDetails(request,pk):
    companydetails=CompanyDetails.objects.get(id=pk)
    form=CompanyDetailsForm(instance=companydetails)
    page="edit"
    if request.method == "POST":
        form=CompanyDetailsForm(request.POST,instance=companydetails)
        if form.is_valid():
            form.save()
            return redirect("custom")

    context={
        "form":form,
        "page":page
    }

    return render(request,"base/add-property.html",context)

def locations(request):
    form=LocationForm()

    if request.method == "POST":
        form=LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("custom")



    context={
        "form":form
    }
    return render(request,"base/location.html",context)

def images(request):
    form=ImagesForm()

    if request.method == "POST":
        form=ImagesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("images")



    context={
        "form":form
    }
    return render(request,"base/images.html",context)
