


from django.urls import path
from . import views


urlpatterns=[
    path("",views.index,name="home"),
    path("custom/",views.panel,name="custom"),
    path("details/<str:pk>/",views.details,name="details"),
    path("add/",views.addproperty,name="add"),
    path("edit/<str:pk>/",views.editProperty,name="edit"),
    path("delete/<str:pk>/",views.deleteProperty,name="delete-item"),
    path("locations",views.locations,name="locations"),
    path("images",views.images,name="images"),

    path("owner/",views.addOwner,name="owner"),
    path("company-details/",views.companyDetails,name="company-details"),
    path("edit-company-details/<str:pk>/",views.editCompanyDetails,name="edit-company-details"),

    path("login-user/",views.loginPage,name="login-user"),
    path("logout-user/",views.logout,name="logout")
]



