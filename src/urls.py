from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from posts import views

from accounts.views import (login_view, logout_view, register_view) 
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include("posts.urls", namespace="posts")),
    url(r'^accounts/login/', login_view, name="login"),
    url(r'^accounts/logout/', logout_view, name="logout"),
    url(r'^accounts/register/', register_view, name="register"),    
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api/users/', include("accounts.api.urls", namespace="users-api")),
    url(r'^api/posts/', include("posts.api.urls", namespace="posts-api")),
    	]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	