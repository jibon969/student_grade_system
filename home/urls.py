from django.urls import path
from .views import (
    home,
    # Program
    program_list,
    add_program,
    update_program,
    delete_program,
    download_program_csv,

    # Status
    status_list,
    add_status,
    update_status,
    delete_status,
    download_status_csv,

    # Student-information
    student_information_list,
    add_student_information,
    update_student_information,
    delete_student_information,
    download_student_information_csv
)

urlpatterns = [
    path('', home, name="home"),

    # Program
    path('program-list/', program_list, name="program-list"),
    path('add-program/', add_program, name="add-program"),
    path('update-program/<int:id>/', update_program, name="update-program"),
    path('delete-program/<int:id>/', delete_program, name="delete-program"),
    path('download-program-csv/', download_program_csv, name="download-program-csv"),

    # Status
    path('status-list/', status_list, name="status-list"),
    path('add-status/', add_status, name="add-status"),
    path('update-status/<int:id>/', update_status, name="update-status"),
    path('delete-status/<int:id>/', delete_status, name="delete-status"),
    path('download-status-csv/', download_status_csv, name="download-status-csv"),

    # Student-information
    path('student-information/', student_information_list, name="student-information"),
    path('add-student-information/', add_student_information, name="add-student-information"),
    path('update-student-information/<int:id>/', update_student_information, name="update-student-information"),
    path('delete-student-information/<int:id>/', delete_student_information, name="delete-student-information"),
    path('download-student-information-csv/', download_student_information_csv, name="download-student-information-csv"),

]
