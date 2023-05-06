from django.db import models


# Create your models here.
class Avatar(models.Model):
    user = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos', default='avatar.jpg')
