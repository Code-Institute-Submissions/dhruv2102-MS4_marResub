from django import forms
from .models import Subscribers


class SubscribeForm(forms.ModelForm):
    """
    Subscribe form
    """

    class Meta:
        """
        Meta
        """

        model = Subscribers
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "email": "Email Address",
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False
