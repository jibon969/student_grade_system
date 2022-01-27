from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Program, Status, StudentInformation


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


# StudentInformation Admin
class StudentInformationResourceCSV(resources.ModelResource):
    class Meta:
        model = StudentInformation
        fields = (
            'id',
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
        )


class StudentInformationAdmin(ImportExportModelAdmin):

    resource_class = StudentInformationResourceCSV
    list_per_page = 20
    list_display = ['status', 'program', 'first_name', 'school_id_number', 'email_address']
    search_fields = ['status', 'program', 'first_name', 'school_id_number', 'email_address']


admin.site.register(StudentInformation, StudentInformationAdmin)