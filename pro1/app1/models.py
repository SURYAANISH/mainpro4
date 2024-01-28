from django.db import models
from django.contrib.auth.models import User
class Dress(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    brand=models.CharField(max_length=250)
    img=models.ImageField(upload_to='gallery')
    material=models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    colour=models.CharField(max_length=250)
    def __str__(self):
        return self.name
# Create your models here.


class CartItem(models.Model):
    product = models.ForeignKey(Dress, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'