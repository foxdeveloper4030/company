# Generated by Django 2.2.12 on 2021-08-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210821_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='public/img/social')),
                ('link', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='employment',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='email',
            field=models.EmailField(max_length=250, unique=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='fist_name',
            field=models.CharField(max_length=250, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='last_name',
            field=models.CharField(max_length=250, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='phone_number',
            field=models.CharField(max_length=250, unique=True, verbose_name='شماره موبایل'),
        ),
    ]
