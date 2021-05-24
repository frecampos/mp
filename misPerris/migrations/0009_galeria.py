# Generated by Django 3.2 on 2021-05-23 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('misPerris', '0008_alter_mascota_dueno'),
    ]

    operations = [
        migrations.CreateModel(
            name='galeria',
            fields=[
                ('auto_inc', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='galeria')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misPerris.mascota')),
            ],
        ),
    ]
