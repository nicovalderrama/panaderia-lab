# Generated by Django 5.1.2 on 2024-10-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='total_monto_venta',
            field=models.FloatField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
