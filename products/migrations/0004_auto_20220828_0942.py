# Generated by Django 3.1.1 on 2022-08-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220812_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='products', to='products.Category'),
        ),
    ]
