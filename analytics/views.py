import json
import numpy as np
import pandas as pd

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render

from reports.models import ItemReport


@login_required
def dashboard(request):

    # Get active reports
    reports = ItemReport.objects.filter(status="ACTIVE")

    # Basic statistics
    total_reports = reports.count()

    total_lost = reports.filter(
        report_type="LOST"
    ).count()

    total_found = reports.filter(
        report_type="FOUND"
    ).count()

    # Found reports percentage
    found_percentage = (
        round((total_found / total_reports) * 100, 1)
        if total_reports > 0
        else 0
    )

    # Category-wise statistics
    category_data = list(
        reports.values("category")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    category_labels = [
        item["category"] or "Uncategorized"
        for item in category_data
    ]

    category_values = [
        item["total"]
        for item in category_data
    ]

    # Average reports per category
    average_category_count = (
        round(float(np.mean(category_values)), 1)
        if category_values
        else 0
    )

    # Monthly lost and found reports
    monthly_data = list(
        reports.annotate(
            month=TruncMonth("event_date")
        )
        .values("month", "report_type")
        .annotate(total=Count("id"))
        .order_by("month")
    )

    # Prepare monthly data using Pandas
    df = pd.DataFrame(monthly_data)

    monthly_labels = []
    monthly_lost = []
    monthly_found = []

    if not df.empty:

        df["month"] = pd.to_datetime(df["month"])

        pivot = df.pivot_table(
            index="month",
            columns="report_type",
            values="total",
            aggfunc="sum",
            fill_value=0
        ).sort_index()

        monthly_labels = [
            date.strftime("%b %Y")
            for date in pivot.index
        ]

        monthly_lost = (
            pivot["LOST"].astype(int).tolist()
            if "LOST" in pivot.columns
            else [0] * len(pivot)
        )

        monthly_found = (
            pivot["FOUND"].astype(int).tolist()
            if "FOUND" in pivot.columns
            else [0] * len(pivot)
        )

    # Recent reports
    recent_reports = ItemReport.objects.order_by("-id")[:5]

    # Dashboard context
    context = {
        "total_reports": total_reports,
        "total_lost": total_lost,
        "total_found": total_found,
        "found_percentage": found_percentage,
        "average_category_count": average_category_count,

        "category_labels_json": json.dumps(category_labels),
        "category_values_json": json.dumps(category_values),

        "monthly_labels_json": json.dumps(monthly_labels),
        "monthly_lost_json": json.dumps(monthly_lost),
        "monthly_found_json": json.dumps(monthly_found),

        "recent_reports": recent_reports,
    }

    return render(
        request,
        "analytics/dashboard.html",
        context
    )