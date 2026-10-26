from django.urls import path
from . import views

urlpatterns = [
    path("", views.browse_items, name="browse_items"),

    path("lost/", views.create_report, name="report_lost"),
    path("found/", views.create_report, name="report_found"),

    path("my/", views.my_reports, name="my_reports"),

    path(
        "edit/<int:pk>/",
        views.edit_report,
        name="edit_report"
    ),

    path(
        "delete/<int:pk>/",
        views.delete_report,
        name="delete_report"
    ),
]