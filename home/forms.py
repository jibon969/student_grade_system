from django import forms
from .models import (
    Program,
    Status,
    StudentInformation
)

from django.forms import Textarea


class DateInput(forms.DateInput):
    input_type = 'date'


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


class StudentInformationModelForm(forms.ModelForm):
    class Meta:
        model = StudentInformation
        fields = [
            'status',
            'program',
            'first_name',
            'middle_name',
            'last_name',
            'former_surname',
            'also_known_as_given_name',
            'date_of_birth',
            'gender',
            'school_id_number',
            'phone_number_home',
            'phone_number_cell',
            'email_address',
            'mailing_address',
            'city_province',
            'postal_code',
            'asn',
            'aboriginal_status',
            'legal_status',
            'enrolment_start_date',
            'enrolment_end_date',
            'enrolment_actual_end',
            'enrolment_grad_code',
            'enrolment_jp_code',
            'enrolment_employer_name',
            'enrolment_employer_contact',
            'enrolment_notes',
        ]

        # Override some fields
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
            'enrolment_start_date': DateInput(attrs={'type': 'date'}),
            'enrolment_end_date': DateInput(attrs={'type': 'date'}),
            'enrolment_actual_end': DateInput(attrs={'type': 'date'}),
            'enrolment_employer_name': Textarea(attrs={'rows': 2, 'cols': 2}),
            'enrolment_employer_contact': Textarea(attrs={'rows': 2, 'cols': 2}),
            'enrolment_notes': Textarea(attrs={'rows': 2, 'cols': 2}),

        }
