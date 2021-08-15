from django.contrib import admin

# Register your models here.
from product.models import Project, TimeLine, File, Pay,Release

admin.site.register(Project)
admin.site.register(TimeLine)
admin.site.register(File)
admin.site.register(Pay)
admin.site.register(Release)