from django.shortcuts import render
from django.views.generic import View

from menu.models import Dish


class MenuView(View):

    def get(self, request):
        menu_sections = [
            {
                'title': 'Specials',
                'dishes': Dish.objects.filter(is_special=True),
            },
            {
                'title': 'Appetizers',
                'dishes': Dish.objects.filter(category='Appetizer'),
            },
            {
                'title': 'Soup or Salad',
                'dishes': Dish.objects.filter(category='Soup or Salad'),
            },
            {
                'title': 'Main Course',
                'dishes': Dish.objects.filter(category='Main Course'),
            },
            {
                'title': 'Dessert',
                'dishes': Dish.objects.filter(category='Dessert'),
            },
        ]
        context = {
            'menu_sections': menu_sections,
        }
        return render(request, 'menu.html', context)
