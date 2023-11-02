from django.contrib import admin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'review_num', 'cut_num', 'date_joined']
    search_fields = ['username', 'email']
    list_filter = ['username', 'first_name', 'last_name', 'email', 'review_num', 'cut_num', 'date_joined']
