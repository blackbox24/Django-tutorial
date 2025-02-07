from django.db import models
from django_tenants.models import TenantMixin,DomainMixin
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20,null=False,blank=False,unique=True)
    description = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.owner.username}"
    

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)

    # Automatically created and synced when it is saved
    auto_create_schema = True

    def __str__(self):
        return self.name
    

class Domain(DomainMixin):
    pass
