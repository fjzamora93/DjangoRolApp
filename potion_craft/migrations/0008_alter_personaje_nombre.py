# Generated by Django 5.0.3 on 2024-03-28 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potion_craft', '0007_personaje_clase_personaje_portrait'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaje',
            name='nombre',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
