# Generated by Django 3.2 on 2022-04-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured_product',
            field=models.BooleanField(default=False),
        ),
    ]
