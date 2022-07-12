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
    name = models.CharField( max_length=254 )
    

    