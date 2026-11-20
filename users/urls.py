from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("profilelogs", LogEntryViewSet, basename="logentry-viewset")

urlpatterns = [
    path(
        "cbv/profiles/",
        ProfileListView.as_view({"get": "list"}),
        name="cbv-profiles",
    ),
    path(
            "nplusone/profiles/",
            ProfileNPlusOneView.as_view(),
            name="nplusone-profiles",
    ),
    path(
        "generics/profiles/",
        ProfileListCreateApiView.as_view(),
        name="generics-profiles",
    ),
    path(
        "generics/profiles/<int:pk>/",
        ProfileRetrieveUpdateDestroyView.as_view(),
        name="generics-profiles-detail",
    ),
    path("viewset/", include(router.urls)),

]
