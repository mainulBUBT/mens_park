from django.db import models

# Create your models here.
SIZE_CHOICES = [
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('M,L,XL', 'M,L,XL'),
]



class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=200)
    gsm = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product_images')
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    made_in = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Outlets(models.Model):
    name = models.CharField(max_length=200)
    cell = models.CharField(max_length=12)
    manager_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200) 
    map_link = models.CharField(max_length=200) 
    embed_link = models.CharField(max_length=1000, null=True)
    opening_hours = models.CharField(max_length=100) 
    closing_hours = models.CharField(max_length=100) 
    off_day = models.CharField(max_length=100)
    image = models.ImageField(upload_to='outlet_images')

    def __str__(self):
        return self.name