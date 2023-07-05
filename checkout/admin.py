from django.contrib import admin
from .models import CheckOut
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CheckoutAdminview(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['first_name','last_name','address']
    list_filter = ['username']

admin.site.register(CheckOut,CheckoutAdminview)
