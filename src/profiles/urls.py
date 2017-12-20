from django.conf.urls import url

from .views import (
    ProfileDetailView,
    activate_user_view
)

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
]