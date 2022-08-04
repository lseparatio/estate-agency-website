from email.headerregistry import Address
from tabnanny import verbose
from zoneinfo import available_timezones
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

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Property_Type(models.Model):

    subcategory = models.ForeignKey(
        'Subcategory', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Property Type'
        verbose_name_plural = 'Property Types'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(
        'Subcategory', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, default='Name is empty')
    description = models.TextField(default='Please provide description')
    price = models.PositiveIntegerField(default="0")
    period = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    primary_image = models.ImageField(null=True, blank=True)
    detail_image1 = models.ImageField(null=True, blank=True)
    detail_image2 = models.ImageField(null=True, blank=True)
    detail_image3 = models.ImageField(null=True, blank=True)
    detail_image4 = models.ImageField(null=True, blank=True)
    detail_image5 = models.ImageField(null=True, blank=True)
    detail_image6 = models.ImageField(null=True, blank=True)
    detail_image7 = models.ImageField(null=True, blank=True)
    detail_image8 = models.ImageField(null=True, blank=True)
    detail_image9 = models.ImageField(null=True, blank=True)
    detail_image10 = models.ImageField(null=True, blank=True)
    detail_image11 = models.ImageField(null=True, blank=True)
    detail_image12 = models.ImageField(null=True, blank=True)
    town = models.CharField(max_length=254, default='Please specify town')
    address = models.CharField(max_length=254, default='Please provide the address')
    post_code = models.CharField(
        max_length=254, default='Please specify post code')
    property_type = models.ForeignKey(
        'Property_Type', null=True, blank=True, on_delete=models.SET_NULL)
    bedroom = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    bathroom = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    reception = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    adults = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    children = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    rooms = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    available = models.BooleanField(default=True, null=True, blank=True)
    rented = models.BooleanField(default=False, null=True, blank=True)
    sold = models.BooleanField(default=False, null=True, blank=True)
    available_from = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
