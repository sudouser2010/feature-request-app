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
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter Title',
                'data-bind': "value: title"
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter Description',
                'data-bind': 'value: description'
            }),
            'client': forms.Select(attrs={
                'data-bind': """
                options: clients,
                optionsText: 'name',
                optionsValue: 'id',
                value: 0,
                optionsAfterRender: setOptionAsDisabled
                """
            }),
            'priority': forms.NumberInput(attrs={
                'min': 1,
                'placeholder': 'Enter Priority',
                'data-bind': 'value: priority'
            }),
            'target_date': forms.DateTimeInput(attrs={
                'type': 'date',
                'data-bind': 'value: date'
            }),
            'ticket_url': forms.TextInput(attrs={
                'placeholder': 'Enter Ticket URL',
                'data-bind': 'value: url'
            }),
            'product_area': forms.Select(attrs={
                'data-bind': """
                options: productArea,
                optionsText: 'name',
                optionsValue: 'id',
                value: 0,
                optionsAfterRender: setOptionAsDisabled
                """
            }),
        }
