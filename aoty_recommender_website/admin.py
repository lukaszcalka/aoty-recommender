from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Album, Artist, Song


class UserAdmin(UserAdmin):
    ordering = ("email",)


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)
