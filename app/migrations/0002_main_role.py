# Generated by Django 2.0 on 2020-08-20 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='role',
            field=models.CharField(default='service', max_length=50),
        ),
    ]