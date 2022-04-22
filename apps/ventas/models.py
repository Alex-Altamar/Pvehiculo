from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Ventas(models.Model):
    fecha = models.Datefield()
    valortotal = models.Bigintegerfield()
    tipopago = models.CharField(max_length=20)
    user = models.foreingKey(User, null= true, blanck= line, on_delete=models.CASCADE)

