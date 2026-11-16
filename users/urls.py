from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("profiles", ProfileView, basename="profiles-viewset")
router.register(
    "ProflieTest", ProflieTestViewSet, basename="profiles-viewset-test"
)
router.register("profilelogs", LogEntryViewSet, basename="logentry-viewset")

urlpatterns = [
    # path('profiles/', profile_list_view, name='profile_list'),
    # path('profiles/', ProfileListView.as_view(), name='profile_list'),
    # path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    # path('subscribe/', Subscribe.as_view(), name='subscribe'),
    path("fbv/profiles/", profile_list, name="fbv-profiles"),
    path(
        "cbv/profiles/",
        ProfileListView.as_view({"get": "list"}),
        name="cbv-profiles",
    ),
    path(
        "cached/profiles/",
        ProfileCachedListView.as_view({"get": "list"}),
        name="cached-profiles",
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
