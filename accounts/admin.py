from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAdminConfig(UserAdmin):

    ordering = ('email', )
    search_fields = ('email', 'first_name', 'last_name')
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    list_filter = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {
            "fields": (
                'email', 'first_name', 'last_name'
            ),
        }),
        ('Permission', {
            'fields':(
                'is_staff', 'is_active', 'is_superuser'
            )
        }
        ),
    )


    add_fieldsets = (
        (None, {
            'classes' : ('wide', ),
            'fields' : ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    

admin.site.register(User, UserAdminConfig)