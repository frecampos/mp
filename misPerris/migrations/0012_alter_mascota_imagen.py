# Generated by Django 3.2 on 2021-05-24 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misPerris', '0011_alter_mascota_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(null=True, upload_to='mascotas'),
        ),
    ]
