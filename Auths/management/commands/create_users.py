# create users
# create groups 
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    
    def handle(self,*args, **options):
        #  create a user and set permission to user
        try:
            if not User.objects.filter(username="user1").exists():
                user1 = User.objects.create_user(
                    username="user1",
                    email="user1@mail.com",
                    password="user@12345"
                )

                self.stdout.write(self.style.SUCCESS("user1 created"))
            
            if not User.objects.filter(username="user2").exists():
                user1 = User.objects.create_user(
                    username="user2",
                    email="user2@mail.com",
                    password="user@12345"
                )

                self.stdout.write(self.style.SUCCESS("user2 created"))
            
            if not User.objects.filter(username="user3").exists():
                user1 = User.objects.create_user(
                    username="user3",
                    email="user3@mail.com",
                    password="user@12345"
                )

                self.stdout.write(self.style.SUCCESS("user3 created"))
        except:
            self.stdout.write(self.style.ERROR("failed to create user"))
        
