# Generated by Django 5.1.5 on 2025-01-21 19:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_product_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='sabad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False, verbose_name='پرداخت شده / نشده')),
                ('pay_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سبدهای خرید',
            },
        ),
        migrations.CreateModel(
            name='sabad_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sabad.sabad')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'جزئیات سبد خرید',
                'verbose_name_plural': 'جزئیات سبدهای خرید',
            },
        ),
    ]
