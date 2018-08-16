from django.contrib import admin
from .models import Laundry

# Register your models here.

class laundryAdmin(admin.ModelAdmin):
    pass



admin.site.register(Laundry, laundryAdmin)
