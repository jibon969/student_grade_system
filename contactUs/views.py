from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ContactForm, ReplayForm
from .models import Contact
from django.conf import settings
from django.db.models import Q
import csv
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from htmlmin.decorators import minified_response


@minified_response
def contact(request):
    """
    This function is work contact
    :param request:
    :return:
    """
    form = ContactForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Success! Thank you for your message.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if form.errors:
        errors = form.errors
    context = {
        'form': form,
        'errors': errors,
    }
    return render(request, 'contactUs/contacts.html', context)


@minified_response
def contact_list(request):
    """
    This function works show all contact list
    :param request:
    :return:
    """
    posts_list = Contact.objects.order_by('-timestamp')[:400]
    query = request.GET.get('q')
    page = request.GET.get('page')
    if query:
        posts_list = Contact.objects.filter(
            Q(subject__icontains=query) |
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query)
        ).distinct()
    paginator = Paginator(posts_list, 10)  # 10 posts per page
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'object_list': posts,
        'page': page
    }
    return render(request, 'contactUs/contact-list.html', context)


@minified_response
def update_contact(request, id):
    """
    This function work for update single update item
    :param request:
    :param id:
    :return:
    """
    page = request.GET.get("page")
    obj = get_object_or_404(Contact, pk=id)
    form = ContactForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Successfully updated Contact info.')
        url = reverse_lazy("contact-list") + "?page=" + page
        return redirect(url)
    return render(request, 'contactUs/contact-update.html', {'form': form})


@minified_response
def delete_contact(request, id):
    """
    This function work for delete single update item
    :param request:
    :param id:
    :return:
    """
    if request.user.is_superuser:
        obj = get_object_or_404(Contact, pk=id)
        context = {
            'obj': obj
        }
        if request.method == "POST":
            obj.delete()
            messages.add_message(request, messages.WARNING, 'Successfully Delete this contact')
            return redirect("contact-list")
        return render(request, "contactUs/delete-contact.html", context)
    else:
        messages.add_message(request, messages.WARNING, 'Only superuser and access this .')
        return redirect('home')


@minified_response
def replay_contact(request):
    if request.method == "POST":
        form = ReplayForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['send_to']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
            form.save()
            messages.success(request, 'your message has been sent')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = ReplayForm()
    return render(request, 'contactUs/replay-email.html', {'form': form})


@minified_response
def download_contact_csv(request):
    queryset = Contact.objects.all()
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow([
        'ID', 'Subject', 'Full Name', 'E-mail', 'Phone', 'Message'
    ])
    for q in queryset:
        row = []
        row.extend([
            q.id, q.subject, q.name, q.email, q.message
        ])
        writer.writerow(row[:])

    response['Content-Disposition'] = 'attachment; filename="contact.csv"'
    return response


