# Generated by Django 2.2.12 on 2021-08-22 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='company',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
