# Generated by Django 5.0.4 on 2024-05-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_producto_descripcion_alter_producto_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('disponible', models.BooleanField(default=True)),
                ('Etiqueta', models.CharField(choices=[('Gluten Free', 'Gluten Free'), ('Vegan', 'Vegan'), ('With Wheat', 'With Wheat'), ('Sugar Free', 'Sugar Free')], default='With Wheat', max_length=20)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(choices=[('Gluten Free', 'Gluten Free'), ('Vegan', 'Vegan'), ('With Wheat', 'With Wheat'), ('Sugar Free', 'Sugar Free')], default='With Wheat', max_length=50),
        ),
    ]