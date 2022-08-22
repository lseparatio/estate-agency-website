from django.contrib import admin
from .models import Category, Subcategory, Product, Property_Type, Order, OrderLineItem


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
        'detail_image11',
        'detail_image12',
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


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                        'order_total',
                       'grand_total',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',
              'order_total', 'grand_total',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Property_Type, Property_TypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
