# Generated by Django 5.1.2 on 2024-10-27 23:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_rename_usuario_venta_user_name_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ventas.venta'),
        ),
    ]
