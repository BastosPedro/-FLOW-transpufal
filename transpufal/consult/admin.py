from django.contrib import admin
from .models import Process, Category

class ProcessAdmin(admin.ModelAdmin):
    list_display = ('name', 'idcode', 'date', 'category', 'archive', 'status')
admin.site.register(Process,ProcessAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category)

# Register your models here.
