# create users
# create groups 
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User

class Command(BaseCommand):
    
    def handle(self,*args, **options):
        #  create a sonar_group and set permission and assin to user
        try:
            if not Group.objects.filter(name="sonar_group").exists():
                group1 = Group.objects.create(
                    name="sonar_group"
                )

                self.stdout.write(self.style.SUCCESS("sonar_group created"))
            else:
                self.stdout.write(self.style.ERROR_OUTPUT("sonar_group already exists"))
        except:
            self.stdout.write(self.style.ERROR("failed to create group"))
        
        # Set Permissions

        try:
            if Permission.objects.filter(codename__contains="sonar").exists():
                sonar_permissions = Permission.objects.filter(codename__contains="sonar")
                new_group = Group.objects.get(name="sonar_group")
                new_group.permissions.set(
                    sonar_permissions
                )
                self.stdout.write(self.style.SUCCESS("sonar_group permissions created"))
            else:
                self.stdout.write(self.style.ERROR_OUTPUT("sonar_group permissions already exists"))

        except:
            self.stdout.write(self.style.ERROR("failed to set Sonar Permission"))


        # Set user to groups
        
        try:
            if User.objects.filter(username="user1").exists():
                user1 = User.objects.get(username="user1")
            else:
                self.stdout.write(self.style.ERROR("user1 does not exist"))

            if Group.objects.filter(name="sonar_group").exists():
                group = Group.objects.filter(name="sonar_group")
                try:
                    sonar_user1_group = user1.groups.get(group_id=group.pk)
                    self.stdout.write(self.style.ERROR("sonar_user1_group already exist"))
                except:
                    sonar_user1_group = user1.groups.set(group)
                    self.stdout.write(self.style.SUCCESS("sonar_user1_group created"))
            else:
                self.stdout.write(self.style.ERROR("sonar_group does not exist"))
        except:
            self.stdout.write(self.style.ERROR("sonar_group does not exist"))
