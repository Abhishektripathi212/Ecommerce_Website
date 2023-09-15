from django.contrib import admin

from shop.models import Category, Products, Tag, Cart


class BaseAdmin(admin.ModelAdmin):
    exclude = ['deleted_at']


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    class Meta:
        model = Category
        fields = '__all__'


@admin.register(Products)
class ProductAdmin(BaseAdmin):
    list_display = ['name', 'price', 'stock']

    class Meta:
        model = Products
        fields = '__all__'


@admin.register(Tag)
class Tag(BaseAdmin):
    class Meta:
        model = Tag
        fields = '__all__'

