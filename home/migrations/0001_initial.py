# Generated by Django 3.1 on 2021-11-10 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Sr', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
