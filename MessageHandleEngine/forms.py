from django import forms
from .models import MessagesModel


class TestForm(forms.ModelForm):
    class Meta:
        model = MessagesModel
        fields = ["message"]
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Type here...",
                    "rows": 4,
                    "columns": 50,
                    "autofocus": "autofocus",
                    "class": "u-border-1 u-border-grey-30 u-input u-input-rectangle u-radius-10"
                }
            )
        }

