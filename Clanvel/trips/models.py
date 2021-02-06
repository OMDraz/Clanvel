from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 
from django.dispatch import receiver 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=254, blank=False)
    first_name = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    interested_in_friends = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save() 


