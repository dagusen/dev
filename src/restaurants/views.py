import random
from django.shortcuts import render
from django.http import HttpResponse

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
	return render(request, "about.html", context)

def contact(request):
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
	return render(request, "contact.html", context)