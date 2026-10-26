from django.contrib import admin
from .models import ItemReport


@admin.register(ItemReport)
class ItemReportAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "report_type",
        "category",
        "color",
        "location",
        "event_date",
        "status",
        "user",
    )

    list_filter = (
        "report_type",
        "category",
        "status",
    )

    search_fields = (
        "title",
        "description",
        "location",
    )