# Generated by Django 5.1.2 on 2024-11-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_rename_precio_producto_precio_lista_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]