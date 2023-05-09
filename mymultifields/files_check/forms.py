from django import forms
from .models import DocCheck


class DocCheckForm(forms.ModelForm):
    class Meta:
        model = DocCheck
        fields = ['title', 'file_mssp', 'file_quotes']