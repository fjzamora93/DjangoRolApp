# Generated by Django 5.0.3 on 2024-03-29 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_userprofile_personajes'),
        ('potion_craft', '0008_alter_personaje_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaje',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personajes', to='accounts.userprofile'),
        ),
    ]
