from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Program, Status


# Program Admin
class ProgramResourceCSV(resources.ModelResource):
    class Meta:
        model = Program
        fields = (
            'id',
            'title'
        )


class ProgramResourceAdmin(ImportExportModelAdmin):

    resource_class = ProgramResourceCSV
    list_per_page = 20
    list_display = ['title']
    search_fields = ['title']


admin.site.register(Program, ProgramResourceAdmin)


# Status Admin
class StatusResourceCSV(resources.ModelResource):
    class Meta:
        model = Status
        fields = (
            'id',
            'title'
        )


class StatusResourceAdmin(ImportExportModelAdmin):

    resource_class = StatusResourceCSV
    list_per_page = 20
    list_display = ['title']
    search_fields = ['title']


admin.site.register(Status, StatusResourceAdmin)