# Generated by Django 4.2.6 on 2023-11-24 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.ImageField(null=True, upload_to='fotos/%Y/%m/%d/'),
        ),
    ]