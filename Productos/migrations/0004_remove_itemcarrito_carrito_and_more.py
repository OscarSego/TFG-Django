# Generated by Django 5.0.3 on 2024-03-12 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_remove_itemcarrito_carrito_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcarrito',
            name='carrito',
        ),
        migrations.RemoveField(
            model_name='itemcarrito',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
        migrations.DeleteModel(
            name='ItemCarrito',
        ),
    ]