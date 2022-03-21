from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.


class UsersAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_admin', 'is_vendor', 'is_customer', 'is_staff', 'last_login')
    search_fields = ('username', 'first_name')
    readonly_fields = ('is_staff', 'last_login', 'date_joined')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()

    ordering = ('username',)


class CustomerSavedListingAdmin(UserAdmin):
    list_display = ('customer', 'business', 'saved_at')
    search_fields = ('business',)
    readonly_fields = ('customer', 'business', 'saved_at')
    filter_horizontal = ()
    list_filter = ('saved_at',)
    fieldsets = ()

    ordering = ('business',)


class NotificationAdmin(UserAdmin):
    list_display = ('title', 'receiver', 'sent_at')
    search_fields = ('title',)
    readonly_fields = ('title', 'receiver', 'sent_at')
    filter_horizontal = ()
    list_filter = ('sent_at',)
    fieldsets = ()

    ordering = ('receiver',)


admin.site.register(User, UsersAdmin)
admin.site.register(Review)
admin.site.register(Business)
admin.site.register(Campus)
admin.site.register(Category)
admin.site.register(Uploads)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(CustomerMessage)
admin.site.register(VendorBusinessRequest)
admin.site.register(CustomerSavedListing, CustomerSavedListingAdmin)
