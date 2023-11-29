from django.shortcuts import render
from rest_framework import generics

from .serializers import *


class OrganizationList(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class SanctionList(generics.ListCreateAPIView):
    queryset = Sanction.objects.all()
    serializer_class = SanctionSerializer


class SanctionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sanction.objects.all()
    serializer_class = SanctionSerializer
