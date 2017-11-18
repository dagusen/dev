import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

# function based view
def home(request):
	num = None
	some_list = [
		random.randint(0,100000000),
		random.randint(0,100000000),
		random.randint(0,100000000)
	]
	condition_bool_item = True
	if condition_bool_item:
		num = random.randint(0,100000000)
	context = {
		"num":num,
		"some_list":some_list
	}
	return render(request, "home.html", context)

def about(request):
	
	return render(request, "about.html",)

def contact(request):
	
	return render(request, "contact.html",)

class ContactView(View):
	def get(self, request, *args, **kwargs):
		print(kwargs)
		context = {

		}
		return render(request, "contact.html", context)