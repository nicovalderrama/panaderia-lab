# Generated by Django 5.1.2 on 2024-10-10 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=255)),
                ('tipo_cliente', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateField()),
                ('tipo_venta', models.CharField(max_length=50)),
                ('forma_pago', models.CharField(max_length=50)),
                ('tipo_comprobante', models.CharField(max_length=50)),
                ('numero_comprobante', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente')),
                ('items', models.ManyToManyField(to='productos.itemventa')),
            ],
        ),
    ]
