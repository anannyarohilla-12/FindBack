import re
from difflib import SequenceMatcher


def normalize(text):
    """Convert text to lowercase and remove extra spaces."""
    if not text:
        return ""

    return re.sub(r"\s+", " ", str(text).strip().lower())


def similarity(text1, text2):
    """Return text similarity as a value between 0 and 1."""
    text1 = normalize(text1)
    text2 = normalize(text2)

    if not text1 or not text2:
        return 0.0

    return SequenceMatcher(None, text1, text2).ratio()


def compare_field(value1, value2):
    """Compare two field values."""
    return similarity(value1, value2)


def calculate_match_score(lost_item, found_item):
    """
    Calculate a score between 0 and 100
    for a Lost report and a Found report.
    """

    weights = {
        "title": 20,
        "category": 25,
        "color": 20,
        "description": 15,
        "location": 15,
        "date": 5,
    }

    scores = {}

    scores["title"] = compare_field(
        lost_item.title,
        found_item.title
    )

    scores["category"] = compare_field(
        lost_item.category,
        found_item.category
    )

    scores["color"] = compare_field(
        lost_item.color,
        found_item.color
    )

    scores["description"] = compare_field(
        lost_item.description,
        found_item.description
    )

    scores["location"] = compare_field(
        lost_item.location,
        found_item.location
    )

    # Date score decreases as the date difference increases.
    days_difference = abs(
        (lost_item.event_date - found_item.event_date).days
    )

    scores["date"] = max(0.0, 1.0 - days_difference / 30)

    total_score = sum(
        scores[field] * weight
        for field, weight in weights.items()
    )

    total_score = round(total_score)

    reasons = []

    for field, score in scores.items():
        if score >= 0.75:
            reasons.append(
                f"Similar {field.replace('_', ' ')}"
            )

    return {
        "score": min(100, max(0, total_score)),
        "reasons": reasons,
        "details": {
            field: round(value * 100)
            for field, value in scores.items()
        },
    }