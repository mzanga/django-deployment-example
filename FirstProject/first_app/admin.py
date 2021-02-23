from django.contrib import admin
from first_app.models import User
from first_app.models import UserProfileInfo

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfileInfo)
