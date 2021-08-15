from django.contrib import admin

# Register your models here.

from home.models import Slider, About, Gallery

admin.site.register(Slider)
#admin.site.register(About)
admin.site.register(Gallery)
