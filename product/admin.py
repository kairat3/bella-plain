from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from .models import Category, Product, Color, Bag, Additional, Size, Favorite


class AdditionalTabularInline(admin.TabularInline):
    model = Additional


class AdditionalAdmin(admin.ModelAdmin):
    model = Additional


class ColorAdmin(admin.ModelAdmin):
    model = Color


class SizeTabularInline(admin.TabularInline):
    model = Size


class SizeAdmin(admin.ModelAdmin):
    model = Size


class ProductAdmin(admin.ModelAdmin):
    inlines = [SizeTabularInline, AdditionalTabularInline, ]
    model = Product


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Bag)
admin.site.register(Additional, AdditionalAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Favorite)
admin.site.unregister(Group)
