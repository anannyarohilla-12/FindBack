from django.db import models
from django.contrib.auth.models import User


class ItemReport(models.Model):

    REPORT_TYPES = [
        ("LOST", "Lost"),
        ("FOUND", "Found"),
    ]

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("CLAIMED", "Claimed"),
        ("RETURNED", "Returned"),
        ("CLOSED", "Closed"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="item_reports"
    )

    report_type = models.CharField(
        max_length=10,
        choices=REPORT_TYPES
    )

    title = models.CharField(max_length=150)

    category = models.CharField(max_length=50)

    color = models.CharField(max_length=50)

    description = models.TextField()

    image = models.ImageField(
        upload_to="items/",
        blank=False
    )

    location = models.CharField(max_length=200)

    event_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.report_type}"

    class Meta:
        ordering = ["-created_at"]