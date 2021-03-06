# Generated by Django 2.2.12 on 2021-08-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210817_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='public/img/companies')),
            ],
        ),
    ]
