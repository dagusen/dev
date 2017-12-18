# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render

from .forms import ItemForm
from .models import Item

# Create your views here.

class ItemListView(ListView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemDetailView(DetailView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemCreateView(CreateView):
	form_class = ItemForm
	template_name = 'form.html'

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		return super(ItemCreateView, self).form_valid(form)

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	# context for html title
	def get_context_data(self, *args, **kwargs):
		context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Create Item'
		return context

class ItemUpdateView(UpdateView):
	form_class = ItemForm
	template_name = 'form.html'
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	# context for html title
	def get_context_data(self, *args, **kwargs):
		context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Update Item'
		return context