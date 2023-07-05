from django.contrib import admin
from .models import product,Reviews
from import_export.admin import ImportExportModelAdmin

class productAdminview(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['name','price','image','qty']
    search_fields=['name','price']
    list_filter=['name','qty','category_name']

class ReviewsAdminview(ImportExportModelAdmin):
    list_display=['product_review','name','email']
    list_filter=['name']

# Register your models here.
admin.site.register(product,productAdminview)
admin.site.register(Reviews,ReviewsAdminview)