from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import ItemReport
from .forms import ItemReportForm


@login_required
def create_report(request):
    if request.method == "POST":
        form = ItemReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()

            messages.success(
                request,
                "Your item report has been submitted successfully!"
            )

            return redirect("browse_items")

    else:
        form = ItemReportForm()

        # Automatically select Lost or Found from the URL.
        requested_type = request.path.rstrip("/").split("/")[-1].upper()

        if requested_type in ["LOST", "FOUND"]:
            form.initial["report_type"] = requested_type

    return render(
        request,
        "reports/report_form.html",
        {"form": form}
    )


def browse_items(request):
    reports = ItemReport.objects.filter(status="ACTIVE")

    report_type = request.GET.get("type", "").strip().upper()
    category = request.GET.get("category", "").strip()
    search = request.GET.get("q", "").strip()

    if report_type in ["LOST", "FOUND"]:
        reports = reports.filter(report_type=report_type)

    if category:
        reports = reports.filter(
            category__icontains=category
        )

    if search:
        reports = reports.filter(
            Q(title__icontains=search)
            | Q(description__icontains=search)
            | Q(location__icontains=search)
        )

    # Calculate display labels in Python, not in template comparisons.
    for item in reports:
        item.display_type = (
            "LOST ITEM"
            if item.report_type == "LOST"
            else "FOUND ITEM"
        )

    return render(
        request,
        "reports/browse_items.html",
        {
            "reports": reports,
            "search": search,
            "category": category,
            "report_type": report_type,
        }
    )


@login_required
def my_reports(request):
    reports = ItemReport.objects.filter(
        user=request.user
    )

    return render(
        request,
        "reports/my_reports.html",
        {"reports": reports}
    )


@login_required
def edit_report(request, pk):
    report = get_object_or_404(
        ItemReport,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        form = ItemReportForm(
            request.POST,
            request.FILES,
            instance=report
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Report updated successfully!"
            )

            return redirect("my_reports")

    else:
        form = ItemReportForm(instance=report)

    return render(
        request,
        "reports/report_form.html",
        {
            "form": form,
            "editing": True,
        }
    )


@login_required
def delete_report(request, pk):
    report = get_object_or_404(
        ItemReport,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        report.delete()

        messages.success(
            request,
            "Report deleted successfully!"
        )

        return redirect("my_reports")

    return render(
        request,
        "reports/confirm_delete.html",
        {"report": report}
    )