from django.contrib import admin
from .models import Profile 

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "email_address", "last_name", "location", "interested_in_friends")

admin.site.register(Profile, ProfileAdmin)