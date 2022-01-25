from django.shortcuts import render
from htmlmin.decorators import minified_response


@minified_response
def dashboard(request):
    return render(request, "dashboard/dashboard.html")