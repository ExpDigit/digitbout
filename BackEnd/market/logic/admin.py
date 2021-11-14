from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    # fields = '__all__'
    prepopulated_fields = {'slug' : ('name',),}

class CatAdmin(admin.ModelAdmin):
    # fields = '__all__'
    prepopulated_fields = {'slug' : ('name',),}



admin.site.register(ProductCategory, CatAdmin)
admin.site.register(OrderPart)
admin.site.register(Product, ProductAdmin)
admin.site.register(Unitsmeasure)
admin.site.register(BotData)
admin.site.register(Properties)
admin.site.register(Farmer)
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(Stock)
admin.site.register(Size)
admin.site.register(Sort)
admin.site.register(Profile)
