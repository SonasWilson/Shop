# Generated by Django 3.2.14 on 2022-09-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default='153'),
            preserve_default=False,
        ),
    ]
