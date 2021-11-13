from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    # fields = '__all__'
    prepopulated_fields = {'slug' : ('name',),}



admin.site.register(ProductCategory)
admin.site.register(OrderPart)
admin.site.register(Product, ProductAdmin)
admin.site.register(Unitsmeasure)
admin.site.register(Properties)
admin.site.register(Status)
admin.site.register(Order)
