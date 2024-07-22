from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class UserAdmin(UserAdmin):
    ordering = ("email",)


admin.site.register(CustomUser, UserAdmin)
