from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE, DO_NOTHING



class ProductCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=1200, verbose_name='Описание категории')
    image = models.ImageField(upload_to='media/prod_cat/')
    stock_multipler = models.FloatField(default=0, verbose_name='Процент скидки по акции')

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'
        ordering = ['name',]

    def __str__(self) -> str:
        return self.name



class Unitsmeasure(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название единицы измерения')

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'



class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название продукта')
    slug = models.SlugField(max_length=20, unique=True, verbose_name='Ссылка в браузере')
    category = models.ForeignKey(ProductCategory, verbose_name='Катогория продукта', on_delete=CASCADE)
    quantity = models.FloatField(verbose_name='Количество товара на складе')
    um = models.ForeignKey(Unitsmeasure, verbose_name='Единицы измерения', on_delete=DO_NOTHING)
    stock_multipler = models.FloatField(default=0, verbose_name='Процент скидки по акции')


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name',]

    def __str__(self) -> str:
        return self.name



class Farmer(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Рекламное название фермера')
    profile = models.OneToOneField(User, verbose_name='Профиль фермера', on_delete=CASCADE)
    
    class Meta:
        verbose_name = 'Статус фермера'
        verbose_name_plural = 'Статус фермеров'



class Size(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name = 'Навание размера')
    
    class Meta:
        verbose_name = 'Размер продукта'
        verbose_name_plural = 'Размеры продуктов'



class Sort(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name = 'Название единицы измерения')
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=CASCADE)
    stock_multipler = models.FloatField(default=0, verbose_name='Процент скидки по акции')

    class Meta:
        verbose_name = 'Сорт продукта'
        verbose_name_plural = 'Сорты продуктов'
        unique_together = ("name", "product")



class Properties(models.Model):
    product_sort = models.ForeignKey(Sort, verbose_name='Продукт-сорт', on_delete=CASCADE)
    farmer = models.ForeignKey(Farmer, verbose_name='Производитель', on_delete=CASCADE)
    year = models.DateField(blank=True, null=True, verbose_name='Год урожая')
    price = models.FloatField(verbose_name='Цена за единицу товара')
    size = models.FloatField(Size)

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

    def __str__(self) -> str:
        return self.name



class OrderPart(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=DO_NOTHING)
    quantity = models.FloatField(verbose_name='Количество')
    price = models.FloatField(verbose_name='Цена в момент покупки')

    class Meta:
        verbose_name = 'Часть заказа'
        verbose_name_plural = 'Части заказов'

    def __str__(self) -> str:
        return str(self.pk) + "_" + self.product.name



class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=CASCADE)
    part = models.ManyToManyField('OrderPart', verbose_name='Часть заказа')
    date = models.DateTimeField(verbose_name='Дата заказа')
    status = models.ForeignKey(Status, verbose_name='Статус заказа', on_delete=DO_NOTHING)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return str(self.pk) + "_" + self.user.username + "_" + self.status.name



class Stock(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название акции')
    text = models.TextField(max_length=1200, verbose_name='Тект новости')
    published = models.BooleanField(default=False, verbose_name='Статус публикации')
    publication_date = models.DateTimeField(verbose_name='Дата публикации')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания новости')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self) -> str:
        return str(self.pk) + "_" + self.name



class Transport(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название транспорта')
    weight = models.CharField(max_length=50, unique=True, verbose_name='Название транспорта')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self) -> str:
        return self.name