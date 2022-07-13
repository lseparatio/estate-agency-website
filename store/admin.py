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
        'image_url',
        'image',
        'town',
        'post_code'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Property_Type, Property_TypeAdmin)
admin.site.register(Product, ProductAdmin)
