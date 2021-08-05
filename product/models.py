from colorfield.fields import ColorField
from django.db import models
from account.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        if not self.parent:
            return f"Category: {self.name}"
        else:
            return f"{self.parent} --> {self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=False)
    preview = models.ImageField(upload_to='images/', blank=True)
    color = models.ManyToManyField(to='product.Color', verbose_name='Цвет', related_name='product_colors')

    def __str__(self):
        return f"{self.category}-->{self.title}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Bag(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bag')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bag')
    quantity = models.PositiveSmallIntegerField(default=1)
    in_bag = models.BooleanField(default=True)

    def __str__(self):
        return {self.user}

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')
    favorite = models.BooleanField(default=True)

    def __str__(self):
        return {self.user}

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class Color(models.Model):
    title = models.CharField(verbose_name='Название цвета', max_length=256)
    color = ColorField(default='#FFFFFF')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвет'


class Additional(models.Model):
    key = models.CharField(max_length=250, blank=True)
    value = models.CharField(max_length=250, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='additional')

    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительная информация'


class Size(models.Model):
    size = models.CharField(max_length=10, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_size')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'