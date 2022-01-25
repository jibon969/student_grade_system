import csv
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from htmlmin.decorators import minified_response
from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Program,
    Status,
)
from .forms import (
    ProgramModelForm,
    StatusModelForm,

)


def home(request):
    return render(request, "home/home.html")


"""---------------------------------------------
            Program List
----------------------------------------------"""


@minified_response
def program_list(request):
    posts_list = Program.objects.all()
    query = request.GET.get('q')
    if query:
        # Using strip method to remove extra white space
        query = query.strip()
        posts_list = Program.objects.filter(
            Q(title__icontains=query)
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
    return render(request, "home/program/program-list.html", context)


@minified_response
def add_program(request):
    if request.method == "POST":
        form = ProgramModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Successfully Added Program')
            return redirect('program-list')
        else:
            messages.add_message(request, messages.warning, 'Please valid information')
            return redirect('add-program')
    else:
        form = ProgramModelForm()
    context = {
        'form': form,
    }
    return render(request, 'home/program/add-program.html', context)


@minified_response
def update_program(request, id):
    page = request.GET.get('page')
    obj = get_object_or_404(Program, pk=id)
    form = ProgramModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Successfully Update Program')
        url = reverse_lazy('program-list') + "?page=" + page
        return redirect(url)
    return render(request, 'home/program/update-program.html', {'form': form})


@minified_response
def delete_program(request, id):
    """
    This function work delete single item form Program list
    :param request:
    :param id:
    :return:
    """
    obj = get_object_or_404(Program, pk=id)
    context = {
        'obj': obj
    }
    if request.method == "POST":
        obj.delete()
        messages.add_message(request, messages.WARNING, 'Successfully Delete Program')
        return redirect("program-list")
    return render(request, "home/program/delete-program.html", context)


@minified_response
def download_program_csv(request):
    queryset = Program.objects.all()
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow([
        'ID', 'Title'
    ])
    for q in queryset:
        row = []
        row.extend([
            q.id, q.title,
        ])
        writer.writerow(row[:])
    response['Content-Disposition'] = 'attachment; filename="program.csv"'
    return response


"""---------------------------------------------
            Status List
----------------------------------------------"""


@minified_response
def status_list(request):
    posts_list = Status.objects.all()
    query = request.GET.get('q')
    if query:
        # Using strip method to remove extra white space
        query = query.strip()
        posts_list = Status.objects.filter(
            Q(title__icontains=query)
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
    return render(request, "home/status/status-list.html", context)


@minified_response
def add_status(request):
    if request.method == "POST":
        form = StatusModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Successfully Added Status')
            return redirect('status-list')
        else:
            messages.add_message(request, messages.warning, 'Please valid information')
            return redirect('add-status')
    else:
        form = StatusModelForm()
    context = {
        'form': form,
    }
    return render(request, 'home/status/add-status.html', context)


@minified_response
def update_status(request, id):
    page = request.GET.get('page')
    obj = get_object_or_404(Program, pk=id)
    form = StatusModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Successfully Update Status')
        url = reverse_lazy('status-list') + "?page=" + page
        return redirect(url)
    return render(request, 'home/status/update-status.html', {'form': form})


@minified_response
def delete_status(request, id):
    """
    This function work delete single item form Status
    :param request:
    :param id:
    :return:
    """
    obj = get_object_or_404(Status, pk=id)
    context = {
        'obj': obj
    }
    if request.method == "POST":
        obj.delete()
        messages.add_message(request, messages.WARNING, 'Successfully Delete Status')
        return redirect("status-list")
    return render(request, "home/status/delete-status.html", context)


@minified_response
def download_status_csv(request):
    queryset = Status.objects.all()
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow([
        'ID', 'Title'
    ])
    for q in queryset:
        row = []
        row.extend([
            q.id, q.title,
        ])
        writer.writerow(row[:])
    response['Content-Disposition'] = 'attachment; filename="status.csv"'
    return response

