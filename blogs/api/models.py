from operator import mod
from pyexpat import model
from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    image = models.ImageField(default='post.jpg', upload_to='post_pics')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']
 
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(max_length=8, blank=True, null=True)
    address = models.TextField(blank=True, default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
 
    def __str__(self):
        return f'{self.user.username} Profile'