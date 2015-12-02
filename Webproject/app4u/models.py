from django.db import models

# Create your models here.

class Images_Real(models.Model):
    real = models.ImageField(upload_to='real')
class Images_Fake(models.Model):
    fake = models.ImageField(upload_to='fake')

