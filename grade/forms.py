from django import forms
from .models import Grade


class GradeModelForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = [
            'name',
            'school_id',
            'email',
            'course_name',
            'teacher_name',
            'completed',
            'marks',
            'letter_grade',
            'file',
            'create_by',
            'updated_by',
        ]
