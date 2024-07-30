from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import LibraryUser, CheckoutLog

@admin.register(LibraryUser)
class LibraryUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id', 'email')
    search_fields = ('name', 'user_id')

@admin.register(CheckoutLog)
class CheckoutLogAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'checkout_date', 'checkin_date')
    search_fields = ('book__title', 'user__name')
    list_filter = ('checkout_date', 'checkin_date')

    
