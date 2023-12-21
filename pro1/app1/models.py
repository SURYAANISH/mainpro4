from django.db import models
from django.db import models
class Dress(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    brand=models.CharField(max_length=250)
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
# Create your models here.
