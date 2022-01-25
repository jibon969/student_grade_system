from django.urls import path
from .views import (
    grade_list,
    add_grade,
    update_grade,
    delete_grade,
    download_grade_csv
)
urlpatterns = [
    path('grade-list/', grade_list, name="grade-list"),
    path('add-grade/', add_grade, name="add-grade"),
    path('update-grade/<int:id>/', update_grade, name="update-grade"),
    path('delete-program/<int:id>/', delete_grade, name="delete-grade"),
    path('download-grade-csv/', download_grade_csv, name="download-grade-csv"),
]
