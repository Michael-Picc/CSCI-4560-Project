from django.urls import path
from .views import *

# These are the browser locations
urlpatterns = [
 path('med_loc/', Med_LocList.as_view()),
 path('med_loc/<int:pk>/', Med_LocDetail.as_view()),
 path('healthInsurance/', HealthInsuranceList.as_view()),
 path('healthInsurance/<int:pk>/', HealthInsuranceDetail.as_view()),
 path('medical_history/', Medical_HistoryList.as_view()),
 path('medical_history/<int:pk>/', Medical_HistoryDetail.as_view()),
 path('doctor/', DoctorList.as_view()),
 path('doctor/<int:pk>/', DoctorDetail.as_view()),
 path('appointment/', AppointmentList.as_view()),
 path('appointment/<int:pk>/', AppointmentDetail.as_view()),
 path('patient/', PatientList.as_view()),
 path('patient/<int:pk>/', PatientDetail.as_view()),
]
