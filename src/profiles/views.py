# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#pulling data from database

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model

from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import DetailView, View, CreateView, ListView

from restaurants.models import RestaurantLocation

from menus.models import Item

from .models import Profile

from .forms import RegisterForm

User = get_user_model()

# Create your views here.


def activate_user_view(request, code=None, *args, **kwargs):
	if code:
		qs = Profile.objects.filter(activation_key=code)
		if qs.exists() and qs.count() == 1:
			profile = qs.first()
			if not profile.activated:
				user_ = profile.user
				user_.is_active = True
				user_.save()
				profile.activated = True
				profile.activation_key = None
				profile.save()
				return redirect("/login")
	# invalid code
	return redirect("/login")

class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'registration/register.html'
	success_url = '/'

	def dispatch(self, *args, **kwargs):
		if self.request.user.is_authenticated():
			return redirect("/logout")
		return super(RegisterView, self).dispatch(*args, **kwargs)

class ProfileFollowToggle(LoginRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		username_to_toggle = request.POST.get("username")
		profile_, is_following = Profile.objects.toggle_follow(request.user, username_to_toggle)
		return redirect('/u/%s' % profile_.user.username )

class ProfileListView(ListView):
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return render(request, "user.html", {})
		user = request.user
		is_following_user_ids = [x.user.id for x in user.is_following.all()]
		qs = Item.objects.filter(user__id__in=is_following_user_ids, public=True).order_by("-updated")[:10]
		# list_
		# for x in user.is_following.all():
		# 	list_.append(x.user.id)

		return render(request, "menus/home-feed.html", {'object_list':qs})

class ProfileDetailView(DetailView):
	template_name = 'profiles/user.html'

	def get_object(self):
		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)

	# search
	def get_context_data(self, *args, **kwargs):
		context =super(ProfileDetailView, self).get_context_data(*args, **kwargs)
		user = context['user']

		#form toggle
		is_following = False
		if user.profile in self.request.user.is_following.all():
			is_following = True
		context['is_following'] = is_following

		query = self.request.GET.get('q')
		item_exists = Item.objects.filter(user=user).exists()
		qs = RestaurantLocation.objects.filter(owner=user).search(query)
		if item_exists and qs.exists():
			context['locations'] = qs
		return context