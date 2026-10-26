from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from reports.models import ItemReport
from .engine import calculate_match_score


@login_required
def my_matches(request):

    # Find all active Lost reports.
    # For testing, include the current user's reports.
    lost_reports = ItemReport.objects.filter(
        user=request.user,
        report_type="LOST",
        status="ACTIVE"
    )

    # Include Found reports from all users,
    # including the current user for testing.
    found_reports = ItemReport.objects.filter(
        report_type="FOUND",
        status="ACTIVE"
    )

    results = []

    for lost_item in lost_reports:

        for found_item in found_reports:

            # Calculate similarity between the two reports.
            match = calculate_match_score(
                lost_item,
                found_item
            )

            # Keep potential matches with a score of 30 or more.
            if match["score"] >= 30:

                results.append({
                    "lost_item": lost_item,
                    "found_item": found_item,
                    "score": match["score"],
                    "reasons": match["reasons"],
                    "details": match["details"],
                })

    # Display the highest-scoring matches first.
    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return render(
        request,
        "matching/my_matches.html",
        {
            "matches": results,
        }
    )