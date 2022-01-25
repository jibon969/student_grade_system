from django import forms
from .models import (
    Program,
    Status,
)


class ProgramModelForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = [
            'title'
        ]


class StatusModelForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'title'
        ]