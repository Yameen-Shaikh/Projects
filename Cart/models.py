from django.db import models
from base.models import BaseModel

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=30, default='shoes', unique=True)
    image = models.ImageField(upload_to = 'product', default='')
    slug = models.SlugField(unique=True, null=True, blank=True)
    

class Product(BaseModel):
    name = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField()
    # image = models.ImageField(upload_to = 'product', default='')


    










