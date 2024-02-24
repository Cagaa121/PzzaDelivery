from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Fillial(models.Model):
    address = models.Charfield(max_legth=200),


    def__str__(self):
        return self.address


class Pizza(models.Model):

    pizza = (
        ('kichik_25', 'Kichik(25)')
        ('ortancha_35', 'Ortancha(25)')
        ('katta_45', 'katta(45)')
    )

    name = models.Charfield(max_legth=100)
    price = models.FloatField(default=0.0
    size = models.Charfield(max_legth=50)
    is_avieable = models.BooleanField(default=True)
    ingredients = models.TextField()
    image = models.ImageField(upload_to='pizza_image/')


    def__str__(self):
        return self.name


class Ordr(models.Model):
    user = models.ForeignKey(USer, on_delete=models.SET_JULL, null=True, blank=True)
    Fillial = models.ForeignKey(on_delete=models.SET_JULL, null=True, blank=True)
    pizza = models.ForeignKey(Pizza, on_delete.CASCADE)
    status = models.Charfield(max_legth=200, choice=STATUS)
    address = models.Charfield(max_legth=150)

    def __str__(self):
        return f"{self.user}"

