# Generated by Django 2.2.12 on 2021-08-16 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='type',
        ),
    ]
