import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import RestaurantLocation

# Create your views here.

def restaurant_listview(request):
	template_name = 'restaurants/restaurant_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class RestaurantListView(ListView):
	queryset = RestaurantLocation.objects.all()
	template_name = 'restaurants/restaurant_list.html'

class SearchRestaurantListView(ListView):
	template_name = 'restaurants/restaurant_list.html'

	def get_queryset(self):
		print(self.kwargs)
		queryset = RestaurantLocation.objects.filter(category__iexact='mexican')
		return queryset