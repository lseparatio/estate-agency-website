from django.contrib import admin
from .models import Category, Subcategory, Product

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

class ProductAdmin(admin.ModelAdmin):
    list_display = (
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
admin.site.register(Product, ProductAdmin)