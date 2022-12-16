from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
                  path("friends/", views.friends, name="friends"),
                  path("delete/<int:pk>/", views.delete_message, name="delete"),
                  path("chat/<int:pk>", views.chat_with_friend, name="chat"),
                  path("singular/<int:pk>", views.user_info, name="user-info"),
                  path("profiles/", views.search_users, name="search-profile"),
                  path("test/", views.test, name="test"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
