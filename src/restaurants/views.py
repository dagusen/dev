from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# function based view
def home(request):
	return HttpResponse("Hello")
	# return render(request, "home.html",{})