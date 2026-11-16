from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    full_name = models.CharField(max_length=300)

    class Role(models.TextChoices):
        STUDENT = "student", _("Student")
        INSTRUCTOR = "instructor", _("Instructor")
        STAFF = "staff", _("Staff")

    role = models.CharField(
        max_length=12, choices=Role.choices, default=Role.STUDENT
    )
    avatar = ResizedImageField(
        size=[256, 256],
        quality=75,
        upload_to="profile-avatars/",
        force_format="JPEG",
        null=True,
        blank=True,
    )
    location = models.CharField(max_length=200, blank=True, null=True)
    course_enrolled = models.PositiveIntegerField(default=0, editable=False)
    course_completed = models.PositiveIntegerField(default=0, editable=False)
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True, editable=False
    )
    github_link = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField()

    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل ها"
        ordering = ("created_at",)

    def __str__(self):
        return str(self.full_name)

auditlog.register(Profile)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def manage_profile(sender, instance, created, **kwargs):
    full_name = f"{instance.first_name} {instance.last_name}".strip()
    if created:
        Profile.objects.create(user=instance, full_name=full_name)
    else:
        Profile.objects.update_or_create(
            user=instance, defaults={"full_name": full_name}
        )
