# -*- coding: utf-8 -*-

from django.urls import path
from . import views
from .views import (ReportListView,
                    DocListView,
                    PatListView,
                    ReportDetailView, 
                    ReportCreateView, 
                    ReportUpdateView, 
                    ReportDeleteView,
                    PatientCreateView,
                    PatientDeleteView,
                    PatientUpdateView,
                    DocReportListView,
                    PatReportListView)


urlpatterns = [
    path('', ReportListView.as_view(), name='Hospital-Home'),
#    path('', views.home, name='Hospital-Home'),
    path('about/', views.about, name='Hospital-About'),
    path('diagreport/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('diagreport/new/', ReportCreateView.as_view(), name='report-create'),
    path('diagreport/<int:pk>/update/', ReportUpdateView.as_view(), name='report-update'),
    path('diagreport/<int:pk>/delete/', ReportDeleteView.as_view(), name='report-delete'),
    path('patient/new/>', PatientCreateView.as_view(), name='patient-create'),
    path('patient/<int:pk>/update/', PatientUpdateView.as_view(), name='patient-update'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),
    path('user/<str:username>/', DocReportListView.as_view(), name='Doc-Report'),
    path('patient/<int:pk>/', PatReportListView.as_view(), name='Pat-Report'),
    path('listdocs/', DocListView.as_view(), name='Doc-List'),
    path('listpats/<str:username>/', PatListView.as_view(), name='Pat-List')
]
