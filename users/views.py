import django_filters.rest_framework as filters
from django.core.cache import cache
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, FormView, ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.throttling import *
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .forms import *
from .models import *
from .serializers import *
from auditlog.models import LogEntry
from rest_framework import viewsets

# def profile_list_view(request):
#     profiles = Profile.objects.select_related('user')
#     return render(request, 'profile_list.html', {'profiles': profiles})

# class ProfileListView2(ListView):
#     model = Profile
#     queryset = Profile.objects.select_related('user')
#     # queryset = Profile.objects.filter(role__exact='student')
#     # queryset = Profile.objects.filter(role__iexact='student')
#     # queryset = Profile.objects.filter(full_name__contains='al')
#     # queryset = Profile.objects.select_related('user').filter(full_name__icontains='Al')
#     template_name = 'profile_list.html'
#     context_object_name = 'profiles'

# def profile_detail_view(request, pk):
#     profile = get_object_or_404(Profile, pk=pk)
#     return render(request, 'profile_detail.html', {'profile': profile})

# class ProfileDetailView(DetailView):
#     model = Profile
#     queryset = Profile.objects.select_related('user')
#     template_name = 'profile_detail.html'
#     context_object_name = 'profile'

# def subscribe(request):
#     if request.method == 'POST':
#         form = UsersForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             print('ثبت شد', email)
#     else:
#         form = UsersForm()

#     return render(request, 'subscribe.html', {'form':form})

# class Subscribe(FormView):
#     template_name = 'subscribe.html'
#     form_class = UsersForm
#     success_url = '/users/subscribe/'

#     def form_valid(self, form):
#         email = form.cleaned_data['email']
#         print('ثبت شد', email)
#         return super().form_valid(form)


@api_view(["GET"])
def profile_list(request):
    profiles = Profile.objects.all()
    serializers_class = ProfileSerializer(profiles, many=True)
    return Response(serializers_class.data)


# class ProfileListView(APIView):
#     throttle_classes = [UserRateThrottle]
#     def get(self, request):
#         profiles = Profile.objects.all()
#         serializers_class = ProfileSerializer(profiles, many=True)
#         return Response(serializers_class.data)


class ProfileFilter(filters.FilterSet):
    course_enrolled_min = filters.NumberFilter(
        field_name="course_enrolled", lookup_expr="gte"
    )
    course_enrolled_max = filters.NumberFilter(
        field_name="course_enrolled", lookup_expr="lte"
    )
    rating_min = filters.NumberFilter(field_name="rating", lookup_expr="gte")
    rating_max = filters.NumberFilter(field_name="rating", lookup_expr="lte")

    class Meta:
        model = Profile
        fields = ["role", "location"]


class ProfilePagination(PageNumberPagination):
    page_size = 2
    page_query_param = "page_size"
    max_page_size = 10


@method_decorator(cache_page(60 * 5), name="dispatch")
class ProfileCachedListView(ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProfileFilter
    search_fields = ["full_name", "github_link"]
    ordering_fields = ["created_at", "rating", "full_name"]
    ordering = ["-created_at"]
    pagination_class = ProfilePagination


class ProfileListView(ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProfileFilter
    search_fields = ["full_name", "github_link"]
    ordering_fields = ["created_at", "rating", "full_name"]
    ordering = ["-created_at"]
    pagination_class = ProfilePagination


class ProfileListCreateApiView(ListCreateAPIView):
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'profile'
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CachedView(APIView):
    def get(self, request):
        data = cache.get("profile_stats")
        if not data:
            total = Profile.objects.count()
            top_rating = Profile.objects.order_by("-rating").first()
            data = {
                "count": total,
                "top_user": top_rating.full_name if top_rating else None,
            }

            cache.set("profile_stats", data, timeout=300)
        return Response(data)


@receiver(post_save, sender=Profile)
def clear_profile_cache(sender, instance, **kwargs):
    cache.delete("profile_stats")
    cache.delete_pattern("views.decorators.cache*")


class ProflieTestViewSet(ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

def profile_list(request):
    profiles = Profile.objects.all()
    for profile in profiles:
        print(profile.user.first_name)

class ProfileNPlusOneView(APIView):
    def get(self, request):
        # profiles = Profile.objects.all()
        profiles = Profile.objects.select_related("user")
        data = []
        for profile in profiles:
            data.append(
                {
                    "full_name": profile.full_name,
                    "user": profile.user.first_name,
                }
            )
        return Response(data)

class LogEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LogEntry.objects.all().select_related("actor", "content_type")
    serializer_class = LogEntrySerializer