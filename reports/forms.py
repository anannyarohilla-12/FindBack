from django import forms
from .models import ItemReport


class ItemReportForm(forms.ModelForm):

    class Meta:
        model = ItemReport

        fields = [
            "report_type",
            "title",
            "category",
            "color",
            "description",
            "image",
            "location",
            "event_date",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={"rows": 4}
            ),

            "event_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }