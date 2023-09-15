from django.db import models

from ecommerce.constants.shops import image_path


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'

        indexes = [
            models.Index(fields=['id', 'deleted_at']),
        ]


class Tag(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'

        indexes = [
            models.Index(fields=['id', 'deleted_at']),
        ]


class Products(BaseModel):
    name = models.CharField(max_length=300)
    price = models.SmallIntegerField()
    stock = models.SmallIntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    tags = models.ManyToManyField(Tag, default=list, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'

        indexes = [
            models.Index(fields=['id', 'deleted_at']),
        ]


class Cart(BaseModel):
    user = models.ForeignKey('authentication.User', on_delete=models.DO_NOTHING, related_name='cart_user')
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    quantity = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'cart'

        indexes = [
            models.Index(fields=['id', 'deleted_at']),
        ]





