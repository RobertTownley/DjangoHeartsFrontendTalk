from django.views.generic import TemplateView

from restaurant.constants import DISH_CATEGORIES
from restaurant.models import Dish


class HomeView(TemplateView):
    template_name = 'restaurant/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['page'] = 'home'
        return context


class AboutView(TemplateView):
    template_name = 'restaurant/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['page'] = 'about'
        return context


class ContactView(TemplateView):
    template_name = 'restaurant/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['page'] = 'contact'
        return context


class MenuView(TemplateView):
    template_name = 'restaurant/menu.html'

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context['page'] = 'menu'
        for category in DISH_CATEGORIES:
            database_category = category[0]
            context[database_category] = Dish.objects.filter(category=database_category)
        return context
