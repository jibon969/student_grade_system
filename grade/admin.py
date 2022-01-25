from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Grade


# Grade Admin
class GradeResourceCSV(resources.ModelResource):
    class Meta:
        model = Grade
        fields = (
            'id',
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
        )


class GradeResourceAdmin(ImportExportModelAdmin):

    resource_class = GradeResourceCSV
    list_per_page = 20
    list_display = ['name', 'school_id', 'email',]
    search_fields = ['name']


admin.site.register(Grade, GradeResourceAdmin)