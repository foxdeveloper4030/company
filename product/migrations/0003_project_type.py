# Generated by Django 2.2.12 on 2021-08-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_project_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.IntegerField(choices=[(1, 'حقیقی'), (2, 'حقوقی')], default=1),
        ),
    ]