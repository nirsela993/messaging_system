from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from user_messages.views import MessageViewSet

router = DefaultRouter()
router.register('user_messages', MessageViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [url('', include(router.urls)),
               ]
