from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)


class Project(models.Model):
    type = [(1, "حقیقی"), (2, "حقوقی")]
    state = [(0, 'پروژه تعریف شد'), (1, 'پروژه تایید شد'), (2, 'در حال ساخت پروژه'), (3, 'اتمام پروژه'),
             (4, 'پروژه تایید نشد')]
    category = models.ForeignKey(Category, on_delete=False, null=True)
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField()
    type = models.IntegerField(choices=type, default=1)
    order_by_fname = models.CharField(max_length=250)
    order_by_lname = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    order_by_tel = models.CharField(max_length=250)
    website = models.CharField(max_length=250, null=False)
    company = models.CharField(max_length=250,null=True)
    state = models.IntegerField(choices=state, default=0)
    created_at = models.DateTimeField(auto_created=True,auto_now=True)
    updated_at = models.DateTimeField(auto_created=True,auto_now=True)


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
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField()
    img = models.ImageField(upload_to='public/img/companies')
