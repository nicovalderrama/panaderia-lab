# Generated by Django 5.1.2 on 2024-10-28 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='unidad',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]