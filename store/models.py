from ast import mod
from tabnanny import verbose
from unicodedata import category
from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Subcategory(models.Model):
    
    class Meta:
        verbose_name_plural = 'Subcategories'

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    subcategory = models.ForeignKey('Subcategory', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, default="Name is empty")
    description = models.TextField(default="Please provide description")
    price = models.DecimalField(max_digits=10, decimal_places=2, default="0")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    town = models.CharField(max_length=254, default="Please specify town")
    post_code = models.CharField(max_length=254, default="Please specify post code")

    def __str__(self):
        return self.name

    

    