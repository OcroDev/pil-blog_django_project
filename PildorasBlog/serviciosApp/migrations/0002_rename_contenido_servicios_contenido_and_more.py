# Generated by Django 4.0.4 on 2022-06-01 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicios',
            old_name='Contenido',
            new_name='contenido',
        ),
        migrations.AlterField(
            model_name='servicios',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]
