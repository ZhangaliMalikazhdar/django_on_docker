from django.shortcuts import render

from .models import Sanction, Organization


def list_excel(request):
    return render(request, 'list.html')
