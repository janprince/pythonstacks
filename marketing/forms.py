from django import forms
from .models import EmailSubscription


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailSubscription
        fields = ('email', )