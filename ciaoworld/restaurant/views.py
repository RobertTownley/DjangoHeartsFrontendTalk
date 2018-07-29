from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'restaurant/home.html'


class AboutView(TemplateView):
    template_name = 'restaurant/about.html'


class ContactView(TemplateView):
    template_name = 'restaurant/contact.html'


class MenuView(TemplateView):
    template_name = 'restaurant/menu.html'
