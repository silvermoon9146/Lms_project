from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'contents', LessonContentViewSet, basename='lessoncontent')

urlpatterns = [
    path('', include(router.urls))

]
