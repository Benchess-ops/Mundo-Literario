# Generated by Django 5.0.6 on 2024-06-22 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_alter_pedido_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]
