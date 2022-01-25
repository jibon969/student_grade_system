import csv
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from htmlmin.decorators import minified_response
from django.shortcuts import render, redirect, get_object_or_404
from .models import Grade
from .forms import GradeModelForm


@minified_response
def grade_list(request):
    posts_list = Grade.objects.all()
    query = request.GET.get('q')
    if query:
        # Using strip method to remove extra white space
        query = query.strip()
        posts_list = Grade.objects.filter(
            Q(name__icontains=query) |
            Q(school_id__icontains=query) |
            Q(email__icontains=query) |
            Q(course_name__icontains=query) |
            Q(teacher_name__icontains=query) |
            Q(completed__icontains=query) |
            Q(letter_grade__icontains=query)
        ).distinct()
    paginator = Paginator(posts_list, 10)  # 5 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'page': page
    }
    return render(request, "grade/grade-list.html", context)


@minified_response
def add_grade(request):
    if request.method == "POST":
        form = GradeModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Successfully Added Grade Information')
            return redirect('grade-list')
        else:
            messages.add_message(request, messages.warning, 'Please valid information')
            return redirect('add-grade')
    else:
        form = GradeModelForm()
    context = {
        'form': form,
    }
    return render(request, 'grade/add-grade.html', context)


@minified_response
def update_grade(request, id):
    page = request.GET.get('page')
    obj = get_object_or_404(Grade, pk=id)
    form = GradeModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Successfully Update Grade Information')
        url = reverse_lazy('grade-list') + "?page=" + page
        return redirect(url)
    return render(request, 'grade/update-grade.html', {'form': form})


@minified_response
def delete_grade(request, id):
    """
    This function work delete single item form Grade list
    :param request:
    :param id:
    :return:
    """
    obj = get_object_or_404(Grade, pk=id)
    context = {
        'obj': obj
    }
    if request.method == "POST":
        obj.delete()
        messages.add_message(request, messages.WARNING, 'Successfully Delete Grade Information')
        return redirect("grade-list")
    return render(request, "grade/delete-grade.html", context)


@minified_response
def download_grade_csv(request):
    queryset = Grade.objects.all()
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow([
        'ID', 'Name', 'School Id', 'Email', 'Course Name', 'Teacher Name', 'Completed',
        'Marks', 'Letter Grade', 'File', 'Create By', 'Updated By',
    ])
    for q in queryset:
        row = []
        row.extend([
            q.id, q.name, q.school_id, q.email, q.course_name, q.teacher_name, q.completed,
            q.marks, q.letter_grade, q.file, q.create_by, q.updated_by
        ])
        writer.writerow(row[:])
    response['Content-Disposition'] = 'attachment; filename="program.csv"'
    return response