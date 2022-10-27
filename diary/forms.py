from django import forms
from diary.models import Diary

class AddDiaryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size':255}))
    body = forms.CharField()

    class Meta:
        model = Diary
        fields = ['title', 'body']