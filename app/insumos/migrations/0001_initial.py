# Generated by Django 5.1.2 on 2024-10-21 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('stock_actual', models.IntegerField()),
                ('punto_pedido', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField()),
                ('fecha_recepcion', models.DateField(blank=True, null=True)),
                ('numero_pedido', models.CharField(max_length=50)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.insumo')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.pedido')),
            ],
        ),
        migrations.AddField(
            model_name='insumo',
            name='proveedor_frecuente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.proveedor'),
        ),
        migrations.CreateModel(
            name='RecepcionPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_recepcion', models.DateField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('pedido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='insumos.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRecepcionPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_recibida', models.IntegerField()),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.insumo')),
                ('recepcion_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.recepcionpedido')),
            ],
        ),
    ]
