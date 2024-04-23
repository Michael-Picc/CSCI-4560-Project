from django.shortcuts import render, redirect
from rest_framework import generics
from .models import *
from .serializers import *
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings

# Create your views here.
def login_page(request):
    #do something
    print('asdf')

'''patient = Pat_Profile.objects.create()
patient.email = 'dodakingdom@gmail.com'
patient.first_name = 'michael'
patient.last_name = 'picchietti'
patient.set_password('ilikepeanuts2')
patient.save() '''


@login_required(login_url="/login/") #need to get login_url
def pat_profile_page(request):
    _email = input()
    profile = Pat_Profile.objects.get(email=_email) #retreives the single email that matches and returns their profile
    return profile.objects

@login_required(login_url="/login/") #need to get login_url
def doc_profile_page(request):
    _email = input()
    profile = Doc_Profile.objects.get(email=_email) #retreives the single email that matches and returns their profile
    return profile.objects







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

class DoctorList(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doc_Profile.objects.all()

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = Doc_Profile.objects.all()

class PatientList(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    queryset = Pat_Profile.objects.all()

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Pat_Profile.objects.all()

class AppointmentList(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

