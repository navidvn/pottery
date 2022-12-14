# Generated by Django 4.1.3 on 2022-12-05 14:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('main_image', models.FileField(upload_to='shop/images')),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductsCategory',
            fields=[
                ('productscategory_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products')),
            ],
            options={
                'db_table': 'ProductsCategory',
            },
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('picture_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.FileField(upload_to='shop/images')),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products')),
            ],
            options={
                'db_table': 'Pictures',
            },
        ),
    ]
