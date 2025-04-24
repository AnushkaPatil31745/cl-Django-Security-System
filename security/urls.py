from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.alert_dashboard, name='alert_dashboard'),
    path('report/', views.report_incident, name='report_incident'),
]
