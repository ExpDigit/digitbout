# Generated by Django 3.2.9 on 2021-11-14 02:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='description',
            field=models.TextField(default='Default description', max_length=1200, verbose_name='Описание категории'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 14, 2, 58, 28, 487240, tzinfo=utc), verbose_name='Дата публикации'),
        ),
    ]
