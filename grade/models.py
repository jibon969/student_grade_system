from django.db import models


class Grade(models.Model):
    name = models.CharField(max_length=200)
    school_id = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    course_name = models.CharField(max_length=150)
    teacher_name = models.CharField(max_length=150)
    completed = models.CharField(max_length=150)
    marks = models.PositiveIntegerField()
    letter_grade = models.CharField(max_length=100)
    file = models.FileField()
    create_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name