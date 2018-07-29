from django.contrib.auth.models import AbstractUser
from django.db import models

from restaurant.constants import DISH_CATEGORIES


class User(AbstractUser):
    '''Custom auth user model representing a site administrator'''
    pass


class Dish(models.Model):
    '''Menu item served up by the restaurant'''
    name = models.CharField(max_length=128)
    price = models.FloatField()
    image = models.ImageField()
    description = models.TextField()
    is_vegetarian = models.BooleanField(default=False)
    is_spicy = models.BooleanField(default=False)
    category = models.CharField(max_length=32, db_index=True, choices=DISH_CATEGORIES)

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name
