# Generated by Django 4.2.6 on 2023-11-24 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_alter_fotografia_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='descricao',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='legenda',
            field=models.CharField(max_length=200),
        ),
    ]
