# Generated by Django 4.0.5 on 2022-07-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='digi',
            field=models.BooleanField(default=False, null=True),
        ),
    ]