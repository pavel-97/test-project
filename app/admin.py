from django.contrib import admin
from .models import Categories, Brand, Products
# Register your models here.

# admin.site.register(Categories)

@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
	pass

@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
	pass

@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
	pass
