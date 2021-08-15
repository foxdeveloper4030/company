# Generated by Django 2.2.12 on 2021-08-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[('1', ''), ('2', '')])),
                ('order_by_fname', models.CharField(max_length=250)),
                ('order_by_lname', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('order_by_tel', models.CharField(max_length=250)),
                ('website', models.CharField(max_length=250)),
                ('company', models.CharField(max_length=250)),
                ('state', models.IntegerField(choices=[(0, 'پروژه تعریف شد'), (1, 'پروژه تایید شد'), (2, 'در حال ساخت پروژه'), (3, 'اتمام پروژه'), (4, 'پروژه تایید نشد')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TimeLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('progress', models.IntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=True, to='product.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='public/img/projects')),
                ('project', models.ForeignKey(on_delete=True, to='product.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('pay_time', models.DateTimeField(null=True)),
                ('state', models.IntegerField(choices=[(0, 'لینک تعریف شد'), (1, 'پرداخت انجام شد'), (2, 'پرداخت ناموفق')])),
                ('Project', models.ForeignKey(on_delete=True, to='product.Project')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('address', models.FileField(upload_to='public/files')),
                ('project', models.ForeignKey(on_delete=True, to='product.Project')),
            ],
        ),
    ]
