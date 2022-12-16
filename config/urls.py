from MessageHandleEngine.views import homepage
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', homepage, name="home"),
    path('messages/', include('MessageHandleEngine.urls')),
    path('users/', include('UsersAuthentication.urls')),
]
