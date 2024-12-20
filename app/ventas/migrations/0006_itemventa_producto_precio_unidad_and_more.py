# Generated by Django 5.1.2 on 2024-11-03 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_alter_itemventa_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemventa',
            name='producto_precio_unidad',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemventa',
            name='tipo_pecio',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
