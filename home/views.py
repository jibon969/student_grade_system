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
    StudentInformation
)
from .forms import (
    ProgramModelForm,
    StatusModelForm,
    StudentInformationModelForm
)


def home(request):
    posts_list = StudentInformation.objects.all()
    search = request.GET.get('q')
    if search:
        # Using strip method to remove extra white space
        query = search.strip()
        posts_list = StudentInformation.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(middle_name__icontains=query) |
            Q(former_surname__icontains=query)
        ).distinct()
    paginator = Paginator(posts_list, 5)  # 5 posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'page': page,
        'search': search,
    }
    return render(request, "home/home.html", context)


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


"""---------------------------------------------
            StudentInformation List
----------------------------------------------"""


@minified_response
def student_information_list(request):
    posts_list = StudentInformation.objects.all()
    query = request.GET.get('q')
    if query:
        # Using strip method to remove extra white space
        query = query.strip()
        posts_list = StudentInformation.objects.filter(
            Q(status__title__icontains=query) |
            Q(program__title__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(middle_name__icontains=query) |
            Q(former_surname__icontains=query) |
            Q(also_known_as_given_name__icontains=query) |
            Q(phone_number_home__icontains=query) |
            Q(phone_number_cell__icontains=query) |
            Q(email_address__icontains=query) |
            Q(mailing_address__icontains=query) |
            Q(city_province__icontains=query) |
            Q(cpostal_code__icontains=query) |
            Q(aboriginal_status__icontains=query) |
            Q(alegal_status__icontains=query) |
            Q(enrolment_employer_name__icontains=query) |
            Q(enrolment_employer_contact__icontains=query)
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
    return render(request, "home/student-information/student-information-list.html", context)


@minified_response
def add_student_information(request):
    if request.method == "POST":
        form = StudentInformationModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Successfully Added Student Information')
            return redirect('student-information')
        else:
            messages.add_message(request, messages.warning, 'Please valid information')
            return redirect('add-student-information')
    else:
        form = StudentInformationModelForm()
    context = {
        'form': form,
    }
    return render(request, 'home/student-information/add-student-information.html', context)


@minified_response
def update_student_information(request, id):
    page = request.GET.get('page')
    obj = get_object_or_404(Program, pk=id)
    form = StudentInformationModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Successfully Update Student Information')
        url = reverse_lazy('student-information') + "?page=" + page
        return redirect(url)
    return render(request, 'home/student-information/update-student-information.html', {'form': form})


@minified_response
def delete_student_information(request, id):
    """
    This function work delete single item form student information
    :param request:
    :param id:
    :return:
    """
    obj = get_object_or_404(StudentInformation, pk=id)
    context = {
        'obj': obj
    }
    if request.method == "POST":
        obj.delete()
        messages.add_message(request, messages.WARNING, 'Successfully Delete Student Information')
        return redirect("student-information")
    return render(request, "home/student-information/delete-student-information.html", context)


@minified_response
def download_student_information_csv(request):
    queryset = StudentInformation.objects.all()
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow([
        'ID', 'Status', 'Program', 'First Name', 'Middle Name', 'Last Name', 'Former Surname',
        'Also known as given name', 'Date of birth', 'Gender', 'School ID Number', 'Phone number home',
        'Phone number cell', 'Email Address', 'Mailing Address', 'City Province', 'Postal Code', 'ASN',
        'Aboriginal Status', 'Legal Status', 'Enrolment Start Date', 'Enrolment End Date', 'Enrolment Actual End',
        'Enrolment grad code', 'Enrolment Employer Name', 'Enrolment Employer Contact', 'Enrolment Notes'

    ])
    for q in queryset:
        row = []
        row.extend([
            q.id, q.status.title, q.program.title, q.first_name, q.middle_name, q.last_name, q.former_surname,
            q.also_known_as_given_name, q.date_of_birth, q.gender, q.school_id_number, q.phone_number_home,
            q.phone_number_cell, q.email_address, q.mailing_address, q.city_province, q.postal_code,
            q.asn, q.aboriginal_status, q.legal_status, q.enrolment_start_date, q.enrolment_end_date,
            q.enrolment_actual_end, q.enrolment_grad_code, q.enrolment_employer_name, q.enrolment_employer_contact,
            q.enrolment_notes
        ])
        writer.writerow(row[:])
    response['Content-Disposition'] = 'attachment; filename="student-information.csv"'
    return response

