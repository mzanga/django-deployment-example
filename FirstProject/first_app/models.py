from django.db import models
from django.contrib.auth.models import User as DUser

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email_address = models.EmailField(max_length=264, unique=True)

    def __str__(self):
        return self.first_name

class UserProfileInfo(models.Model):

    user = models.OneToOneField(DUser, on_delete=models.CASCADE)

    # additional fields
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username
