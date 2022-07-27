from django.contrib import admin
from .models import Category, Subcategory, Product, Property_Type


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class Property_TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'subcategory',
        'name',
        'description',
        'price',
        'period',
        'image_url',
        'primary_image',
        'detail_image1',
        'detail_image2',
        'detail_image3',
        'detail_image4',
        'detail_image5',
        'detail_image6',
        'detail_image7',
        'detail_image8',
        'detail_image9',
        'detail_image10',
        'town',
        'address',
        'post_code',
        'property_type',
        'bedroom',
        'bathroom',
        'reception',
        'adults',
        'children',
        'rooms',
        'available',
        'rented',
        'sold',
        'available_from'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Property_Type, Property_TypeAdmin)
admin.site.register(Product, ProductAdmin)
