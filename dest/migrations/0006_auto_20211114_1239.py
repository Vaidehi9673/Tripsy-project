# Generated by Django 3.1 on 2021-11-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dest', '0005_auto_20211113_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(upload_to='hotel/'),
        ),
    ]
