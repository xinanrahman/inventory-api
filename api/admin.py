from django.contrib import admin
from . import models 

admin.site.site_header = "Custom"

# Register your models here.
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["title", "stock_quantiy", "rating", "price", "in_stock"]
    list_editable = ["stock_quantiy", "price", "in_stock"]
