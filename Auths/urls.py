from django.urls import path
from .views import *
app_name= "auths"
urlpatterns =[
    path("login",CustomLogin,name="custom-login")
]