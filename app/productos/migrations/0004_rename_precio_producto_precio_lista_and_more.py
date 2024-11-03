# Generated by Django 5.1.2 on 2024-11-03 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_alter_producto_cantidad_disponible'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio',
            new_name='precio_lista',
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_mayorista',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]