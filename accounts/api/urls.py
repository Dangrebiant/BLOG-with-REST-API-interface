from django.conf.urls import url
from django.contrib import admin

from .views import(
	#UserDetailAPIView,
	UserCreateAPIView,
	UserLoginAPIView,
		)

urlpatterns = [
	#url(r'^(?P<pk>\d+)/$', UserDetailAPIView.as_view(), name = 'detail'),
	url(r'^login/$', UserLoginAPIView.as_view(), name = 'login'),
	url(r'^register/$', UserCreateAPIView.as_view(), name = 'register'),
	]