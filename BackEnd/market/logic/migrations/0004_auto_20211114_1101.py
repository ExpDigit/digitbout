# Generated by Django 3.2.9 on 2021-11-14 06:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logic', '0003_auto_20211114_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 14, 6, 1, 41, 523686, tzinfo=utc), verbose_name='Дата публикации'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('M', 'Мужской'), ('W', 'Женский')], default='M', max_length=1, verbose_name='Пол')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
