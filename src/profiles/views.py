# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#pulling data from database
from django.contrib.auth import get_user_model

from django.http import Http404

from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView

from restaurants.models import RestaurantLocation

from menus.models import Item

User = get_user_model()

# Create your views here.

class ProfileDetailView(DetailView):
	template_name = 'profiles/user.html'

	def get_object(self):
		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)

	# search
	def get_context_data(self, *args, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
		user = context['user']
		query = self.request.GET.get('q')
		item_exists = Item.objects.filter(user=user).exists()
		qs = RestaurantLocation.objects.filter(owner=user).search(query)	
		if item_exists and qs.exists():
			context['locations'] = qs
		return context