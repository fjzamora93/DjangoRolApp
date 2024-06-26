# Generated by Django 5.0.3 on 2024-03-28 15:40

import accounts.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile'),
        ('potion_craft', '0007_personaje_clase_personaje_portrait'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='personajes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='potion_craft.personaje'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nombre',
            field=models.CharField(default=accounts.models.generate_unique_name, max_length=100),
        ),
    ]
