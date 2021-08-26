from django.db import models
from django.contrib import admin
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='نام عکس')

    def __str__(self):
        return self.name


class Project(models.Model):
    type = [(1, "حقیقی"), (2, "حقوقی")]
    state = [(0, 'پروژه تعریف شد'), (1, 'پروژه تایید شد'), (2, 'در حال ساخت پروژه'), (3, 'اتمام پروژه'),
             (4, 'پروژه تایید نشد')]
    category = models.ForeignKey(Category, on_delete=False, null=True, verbose_name='دسته بندی')
    name = models.CharField(max_length=250, verbose_name='نام')
    title = models.CharField(max_length=250, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    type = models.IntegerField(choices=type, default=1, verbose_name='نوع مشتری')
    order_by_fname = models.CharField(max_length=250, verbose_name='سفارش با نام')
    order_by_lname = models.CharField(max_length=250, verbose_name='سفارش با نام خانوادگی')
    address = models.CharField(max_length=250, verbose_name='آدرس')
    order_by_tel = models.CharField(max_length=250, verbose_name='سفارش با تلفن')
    website = models.CharField(max_length=250, null=False, verbose_name='وب سایت')
    company = models.CharField(max_length=250, null=True, verbose_name='شرکت')
    state = models.IntegerField(choices=state, default=0, verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_created=True, auto_now=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.name


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'title',)


class TimeLine(models.Model):
    project = models.ForeignKey(Project, on_delete=True)
    progress = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_created=True)


class File(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    project = models.ForeignKey(Project, on_delete=True)
    address = models.FileField(upload_to='public/files', validators=[])

    def __str__(self):
        return self.title


class Pay(models.Model):
    state = [(0, 'لینک تعریف شد'), (1, 'پرداخت انجام شد'), (2, 'پرداخت ناموفق')]
    Project = models.ForeignKey(Project, on_delete=True)
    link = models.CharField(max_length=250)
    price = models.IntegerField()
    pay_time = models.DateTimeField(null=True)
    state = models.IntegerField(choices=state)


class Release(models.Model):
    project = models.ForeignKey(Project, on_delete=True)
    img = models.ImageField(upload_to='public/img/projects')

    def __str__(self):
        return self.project.name


class Company(models.Model):
    name = models.CharField(max_length=250, verbose_name='نام')
    title = models.CharField(max_length=250, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    img = models.ImageField(upload_to='public/img/companies', verbose_name='عکس')

    def __str__(self):
        return self.name
