from django.db import models

class Images_Real(models.Model):
    real = models.ImageField(upload_to='real')
class Images_Fake(models.Model):
    fake = models.ImageField(upload_to='fake')


# Create your models here.
