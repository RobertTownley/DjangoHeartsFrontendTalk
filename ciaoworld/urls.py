from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from menu.views import MenuView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('menu', MenuView.as_view(), name='menu'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
