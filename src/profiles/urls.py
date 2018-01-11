from django.conf.urls import url

from .views import (
    ProfileDetailView,
    ProfileListView
)

urlpatterns = [
	url(r'^$', ProfileListView.as_view(), name='list'),
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]