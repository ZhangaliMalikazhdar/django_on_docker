from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_excel, name='all'),
    path('<pk>', views.sanc, name='sanction')
]
