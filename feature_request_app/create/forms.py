from django import forms

from .models import FeatureRequest


class FeatureRequestForm(forms.ModelForm):

    class Meta:
        model = FeatureRequest
        fields = [
            'title',
            'description',
            'client',
            'priority',
            'target_date',
            'ticket_url',
            'product_area'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title'}),
            'description': forms.TextInput(attrs={'placeholder': 'Enter Description'}),
            'target_date': forms.TextInput(attrs={'placeholder': 'Enter Target Date'}),
            'priority': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Enter Priority'}),
            'ticket_url': forms.TextInput(attrs={'placeholder': 'Enter Ticket URL'}),
            }
