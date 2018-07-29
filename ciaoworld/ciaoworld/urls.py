from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from restaurant.views import AboutView
from restaurant.views import ContactView
from restaurant.views import HomeView
from restaurant.views import MenuView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('menu', MenuView.as_view(), name='menu'),
    path('admin/', admin.site.urls),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT,
)
