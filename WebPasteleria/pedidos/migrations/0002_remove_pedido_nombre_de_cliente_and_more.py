# Generated by Django 5.0.4 on 2024-04-21 20:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='nombre_de_cliente',
        ),
        migrations.AddField(
            model_name='pedido',
            name='nombre_de_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuarios', to=settings.AUTH_USER_MODEL),
        ),
    ]