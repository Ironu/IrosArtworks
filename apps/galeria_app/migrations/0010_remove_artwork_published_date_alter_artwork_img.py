# Generated by Django 4.1.3 on 2023-02-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria_app', '0009_artwork_delete_artworks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='artwork',
            name='img',
            field=models.ImageField(blank=True, help_text='Seleccione una imagen para mostrar', null=True, upload_to='Artwork'),
        ),
    ]
