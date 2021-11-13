from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE, DO_NOTHING



class ProductCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=1200, verbose_name='Описание категории')
    image = models.ImageField(upload_to='media/prod_cat/')

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'
        ordering = ['name',]

    def __str__(self) -> str:
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название продукта')
    slug = models.SlugField(max_length=20, unique=True, verbose_name='Ссылка в браузере')
    category = models.ForeignKey(ProductCategory, verbose_name='Катогория продукта', on_delete=CASCADE)
    quantity = models.FloatField(verbose_name='Количество товара на складе')
    price = models.FloatField(verbose_name='Цена за единицу товара')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name',]

    def __str__(self) -> str:
        return self.name



class Unitsmeasure(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название единицы измерения')

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'



class Properties(models.Model):
    um = models.ManyToManyField(Unitsmeasure, verbose_name='Характеристики с фиксированными значениями')
    year = models.DateField(verbose_name='Год урожая')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'



class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=CASCADE)
    quantity = models.FloatField(verbose_name='Количество товара на складе')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'



class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название статуса')

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'



class OrderPart(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=DO_NOTHING)
    quantity = models.FloatField(verbose_name='Количество')
    price = models.FloatField(verbose_name='Цена в момент покупки')

    class Meta:
        verbose_name = 'Часть заказа'
        verbose_name_plural = 'Части заказов'



class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=CASCADE)
    part = models.ManyToManyField('OrderPart', verbose_name='Часть заказа')
    date = models.DateTimeField(verbose_name='Дата заказа')
    status = models.ForeignKey(Status, verbose_name='Статус заказа', on_delete=DO_NOTHING)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



