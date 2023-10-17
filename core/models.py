from django.db import models
from .model_states import *


def get_path_profile_image(instance, filename):
    return 'profile_images/{0}/{1}'.format(instance.user.username, filename)

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER, null=True, blank=True)
    other_gender = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    profile_image = models.ImageField(upload_to=get_path_profile_image, verbose_name="Profile Image", default="default.png")
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profiles'
        
    def __str__(self):
        return 'User Profile from %s %s'%(self.user.first_name, self.user.last_name)