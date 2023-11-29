from django.urls import path
from .views import *

urlpatterns = [
    path('organizations/', OrganizationList.as_view(), name='organization-list'),
    path('organizations/<int:pk>/', OrganizationDetail.as_view(), name='organization-detail'),
    path('sanctions/', SanctionList.as_view(), name='sanction-list'),
    path('sanctions/<int:pk>/', SanctionDetail.as_view(), name='sanction-detail'),
]
