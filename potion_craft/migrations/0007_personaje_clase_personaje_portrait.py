# Generated by Django 5.0.3 on 2024-03-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potion_craft', '0006_alter_potion_alteracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaje',
            name='clase',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='personaje',
            name='portrait',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
