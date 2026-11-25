from django.db import models
from django.conf import settings
from django.utils import timezone

class Course(models.Model):
    class Level(models.TextChoices):
        BEGINNER = 'beginner', 'مقدماتی',
        INTERMIDIATE = 'intermidiate', 'متوسط',
        ADVANCED = 'advanced', 'پیشرفته',
    class Status(models.TextChoices):
        DRAFT = 'draft', 'پیش نویس',
        PUBLISHED = 'published', 'منتشر شده'

    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='courses_related',

    )
    title = models.CharField(max_length=300)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='courses-thumbnail/')
    level = models.CharField(max_length=20, choices=Level.choices, default=Level.INTERMIDIATE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    price = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class CourseVideo(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=300)
    video_file = models.FileField(upload_to='courses-videos/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

class Enrollment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'course']

class Invoice(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'در انتظار پرداخت'
        PAID = 'paid', 'پرداخت شده'
        FAILED = 'failed', 'ناموفق'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    payment_reference = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        ordering = ['created_at']

    def mark_paid(self, reference_code):
        self.status = self.Status.PAID
        self.paid_at = timezone.now()
        self.payment_reference = reference_code
        self.save()