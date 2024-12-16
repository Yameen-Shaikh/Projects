from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel

# Create your models here.

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_emial_valid = models.BooleanField(default=False)
    email_token = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile ')
