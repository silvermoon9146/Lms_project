from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("", NotificationListView.as_view(), name="notification"),
]
