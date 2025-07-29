from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Event
import datetime

class EventForm(forms.ModelForm):
    """
    Form for creating and editing events with validation.
    """

    class Meta:
        model = Event
        fields = ['name', 'description', 'start_date', 'end_date', 'location', 'mode', 'organizer', 'color', 'capacity']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # dodanie klas Bootstrap do wszystkich pól
        for field_name, field in self.fields.items():
            if field_name == 'mode':
                field.widget.attrs['class'] = 'form-select'
            elif field_name == 'color':
                field.widget.attrs['class'] = 'form-control form-control-color'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # 1️⃣ Walidacja: Data zakończenia musi być po dacie rozpoczęcia
        if start_date and end_date and end_date <= start_date:
            raise forms.ValidationError(_('Data zakończenia musi być późniejsza niż data rozpoczęcia.'))

        # 2️⃣ Walidacja: sensowny rok (np. pomiędzy 1900 a 2100)
        for field_name in ['start_date', 'end_date']:
            date_value = cleaned_data.get(field_name)
            if date_value and (date_value.year < 1900 or date_value.year > 2100):
                raise forms.ValidationError(_('Rok w polach daty musi być pomiędzy 1900 a 2100.'))

        return cleaned_data
