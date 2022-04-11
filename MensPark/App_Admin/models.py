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
    description = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    