from django.test import TestCase
from allauth.account.views import login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import requests


# Create your tests here.
class AllauthTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="user1",
            email="nicardid@gmail.com",
            password="nasa@django24"
        )
   
    def test_setup_user_exit(self):
        user_exists = User.objects.filter(username="user1").exists()
        self.assertTrue(user_exists)

    @csrf_exempt
    def test_login_by_email(self):
        request = requests.post(url="http://127.0.0.1:8000/accounts/login/",data={"csrfmiddlewaretoken":"FSra7dKJvQRTFJ9k4E1KosZ5iABRA05tddOxBj97xP8NzdNaNeMRv8pYYtLmo6Yb","username":"nelso","password":"nasa@django24"},)
        is_login = login(request)
        self.assertTrue(is_login)