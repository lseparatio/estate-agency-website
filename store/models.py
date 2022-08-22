import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField
from accounts.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subcategories'

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=254, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

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
    available_from = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0


        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

    
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    lineitem_total = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True, editable=True)

    def save(self, *args, **kwargs):

        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f' {self.order.order_number}'