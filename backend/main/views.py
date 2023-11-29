from django.shortcuts import render

from .models import Sanction, Organization


def list_excel(request):
    orgs = Organization.objects.all()
    sancs = Sanction.objects.all()
    context = {'orgs': orgs, 'sancs': sancs}
    return render(request, 'list.html', context)


def sanc(request, pk):
    org = Organization.objects.get(pk=pk)
    sancs = Sanction.objects.filter(name=org.name)
    context = {'sancs': sancs}
    return render(request, 'sanction.html', context)