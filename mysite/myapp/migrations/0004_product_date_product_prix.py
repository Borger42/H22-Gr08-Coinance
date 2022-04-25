# Generated by Django 4.0.3 on 2022-04-25 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_product_date_remove_product_prix'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prix',
            field=models.FloatField(null=True),
        ),
    ]
