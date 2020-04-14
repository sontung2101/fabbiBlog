from django.contrib import admin
from .models import *


# Register your models here.

# class PersonAdmin(admin.ModelAdmin):
#     model = PersonModel
#     list_display = ['id', 'first_name', 'mid_name', 'last_name',
#                     'is_active', 'is_deleted', 'created_at', 'department']
#     list_filter = ['department', 'is_active']
#     search_fields = ['first_name']
#     readonly_fields = ['department', 'is_active']