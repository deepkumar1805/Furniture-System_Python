from django.contrib import admin
from .models import Contactus
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ContactusAdminview(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['name','email','subject']

admin.site.register(Contactus,ContactusAdminview)