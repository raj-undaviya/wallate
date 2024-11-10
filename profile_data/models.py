from django.db import models

# Create your models here.
class user_profile(models.Model):
    class Meta:
        db_table = 'user_tb'
    user_id = models.CharField(max_length=60, primary_key=True)
    first_name = models.CharField(max_length=120, null=True, blank=True, default=None)
    last_name = models.CharField(max_length=120, null=True, blank=True, default=None)
    username = models.CharField(max_length=120, null=True, blank=True, default=None)
    email = models.CharField(max_length=120, null=True, blank=True, default=None)
    password = models.CharField(max_length=120, null=True, blank=True, default=None)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)