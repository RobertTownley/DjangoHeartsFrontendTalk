from django.shortcuts import render
from django.views.generic import View


class MenuView(View):

    def get(self, request):
        context = {}
        return render(request, 'menu.html', context)
