from dataclasses import field
from django import forms
from .models import Notes

class addNotesForm(forms.ModelForm):
    sender = forms.CharField(widget=forms.TextInput())
    title = forms.CharField(widget=forms.TextInput())
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':'3'}))
    class Meta:
        model = Notes
        fields = ('sender','title','notes')