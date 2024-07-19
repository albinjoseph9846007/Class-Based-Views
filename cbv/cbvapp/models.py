from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    ceo =models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    product_name =models.CharField(max_length=100)
    price =models.IntegerField()
    colour =models.CharField(max_length=100)
    fuel_type =models.CharField(max_length=100)
    milage =models.IntegerField()
    seat_capacity =models.IntegerField()
    company = models.ForeignKey(Company,related_name='companies',on_delete=models.CASCADE)
    car_image =models.ImageField(upload_to='cars/',blank=True,null=True)
    rate= models.IntegerField()

    def __str__(self):
        return self.product_name

