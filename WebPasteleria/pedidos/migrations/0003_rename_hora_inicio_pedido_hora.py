# Generated by Django 5.0.4 on 2024-04-22 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_remove_pedido_nombre_de_cliente_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='hora_inicio',
            new_name='hora',
        ),
    ]
