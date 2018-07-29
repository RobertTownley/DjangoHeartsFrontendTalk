from django.contrib import admin

from restaurant.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
