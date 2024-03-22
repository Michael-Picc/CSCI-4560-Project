from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class Medical_HistoryList(generics.ListAPIView):
    serializer_class = Medical_HistorySerializer

    queryset = Medical_History.objects.all()

class Medical_HistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Medical_HistorySerializer
    queryset = Medical_History.objects.all()

class Med_LocList(generics.ListCreateAPIView):
    serializer_class = Med_LocSerializer
    queryset = Med_Loc.objects.all()

class Med_LocDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Med_LocSerializer
    queryset = Med_Loc.objects.all()

class HealthInsuranceList(generics.ListCreateAPIView):
    serializer_class = HealthInsuranceSerializer
    queryset = Health_Insurance.objects.all()

class HealthInsuranceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HealthInsuranceSerializer
    queryset = Health_Insurance.objects.all()

class DoctorList(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class PatientList(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class AppointmentList(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()