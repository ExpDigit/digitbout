from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import CASCADE, DO_NOTHING



class ProductCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Ссылка в браузере')
    description = models.TextField(max_length=1200, verbose_name='Описание категории')
    image = models.ImageField(upload_to='prod_cat/images/', verbose_name="Изображение продукта")
    stock_multipler = models.FloatField(default=0, verbose_name='Процент скидки по акции')

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'
        ordering = ['name',]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('cat')


class Unitsmeasure(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название единицы измерения')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'



class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название продукта')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Ссылка в браузере')
    category = models.ForeignKey(ProductCategory, verbose_name='Катогория продукта', on_delete=CASCADE)
    um = models.ForeignKey(Unitsmeasure, verbose_name='Единицы измерения', on_delete=DO_NOTHING)
    stock_multipler = models.FloatField(default=0, verbose_name='Процент скидки по акции')
    image = models.ImageField(upload_to='products/images/', verbose_name='Изображение продукта')


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name',]

    def __str__(self) -> str:
        return self.name



class Farmer(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name = 'Рекламное название фермера')
    profile = models.OneToOneField(User, verbose_name='Профиль фермера', on_delete=CASCADE)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Статус фермера'
        verbose_name_plural = 'Статус фермеров'



class Size(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name = 'Навание размера')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Размер продукта'
        verbose_name_plural = 'Размеры продуктов'



class Sort(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name = 'Название сорта')
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=CASCADE)
    stock_multipler = models.FloatField(default=0, verbose_name='Процент скидки по акции')
    image = models.ImageField(upload_to='products/sort/images/', verbose_name='Изображение сорта продукта', blank=True) 

    def __str__(self) -> str:
        return self.name

    def get_name(self) -> str:
        return str(self.product.name) + " " + str(self.name)

    def get_absolute_url(self):
        return reverse_lazy('sort', args=(self.product.slug, self.pk,))

    class Meta:
        verbose_name = 'Сорт продукта'
        verbose_name_plural = 'Сорты продуктов'
        unique_together = ("name", "product")



class Properties(models.Model):
    sort = models.ForeignKey(Sort, verbose_name='Сорт продукта', on_delete=CASCADE)
    farmer = models.ForeignKey(Farmer, verbose_name='Производитель', on_delete=CASCADE)
    quantity = models.FloatField(verbose_name='Количество товара на складе')
    year = models.DateField(blank=True, null=True, verbose_name='Год урожая')
    size = models.ForeignKey(Size, verbose_name="Размер", on_delete=DO_NOTHING)
    stock_multipler = models.FloatField(default=0, verbose_name='Процент скидки по акции')
    price = models.FloatField(verbose_name='Цена за единицу товара')

    def get_name(self) -> str:
        return str(self.sort.product.name) + " " + str(self.sort.name) + " " + (self.size.name)

    def get_price_clear(self):
        return self.price * (1 - float(max(self.stock_multipler, self.sort.stock_multipler, self.sort.product.stock_multipler, self.sort.product.category.stock_multipler)) / float(100))

    def get_price(self) -> str:
        return str(self.get_price_clear(self)) + " руб/" + self.sort.product.um.name

    def get_stock_clear(self):
        return max(self.stock_multipler, self.sort.stock_multipler, self.sort.product.stock_multipler, self.sort.product.category.stock_multipler)

    def get_stock(self):
        return str(self.get_stock_clear(self)) + "%"

    def __str__(self) -> str:
        return self.sort.product.name + "_" + self.sort.name + "_" + self.size.name

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
    publication_date = models.DateTimeField(default=timezone.now(), verbose_name='Дата публикации')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания новости')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self) -> str:
        return str(self.pk) + "_" + self.name



class Transport(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название транспорта')
    weight = models.IntegerField(verbose_name='Грузоподъемность')

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'

    def __str__(self) -> str:
        return self.name


class BotData(models.Model):
    user_id = models.CharField(max_length=20, unique=True, verbose_name='Идентификатор в телеграмме')

    class Meta:
        verbose_name = 'Данные бота'
        verbose_name_plural = 'Данные ботов'

    def __str__(self) -> str:
        return 'user_' + self.user_id