from django.contrib import admin

from menu.models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass
