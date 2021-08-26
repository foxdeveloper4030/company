from django.contrib import admin

# Register your models here.
from product.models import TimeLine, File, Pay, Release, Category, Company

# admin.site.register(Project)
admin.site.register(TimeLine)
admin.site.register(File)
admin.site.register(Pay)
admin.site.register(Release)
admin.site.register(Category)
admin.site.register(Company)