from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f'courses', CourseViewSet, basename='courses')

urlpatterns = [
    # path("enroll/", EnrollInCourseView.as_view(), name="course-enroll"),
    path("payment/invoice/", CreateInvoiceView.as_view(), name="create-invoice"),
    path("payment/invoice/<int:invoice_id>", PayInvoiceView.as_view(), name="pay-invoice"),
    path("my-enrollments/", UserEnrolledCourseView.as_view(), name="my-enrollments"),
    path("recommended/", RecommendedCourseView.as_view(), name="recommended-courses"),
    path('', include(router.urls))


]
