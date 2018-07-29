from django.contrib import admin

from restaurant.models import Dish
from restaurant.models import User


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ['category']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
