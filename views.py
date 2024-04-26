from django.shortcuts import render, redirect
from rest_framework import generics
from .models import *
from .serializers import *
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib import messages
from myapp.models import Profile
from django.contrib.auth import authenticate, login





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


def home(request):
    return render(request, 'homepage.html')
def loginfunc(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        profile = authenticate(email=email, password=password)
        if profile is not None:
            login(request, profile)
            fname = profile.first_name
            lname = profile.last_name
            return render(request, "PatientHomepage.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')


    return render(request, 'homepage.html')
def choice(request):
    return render(request, 'choice.html')
def DRsignUp(request):
    return render(request, 'DRsignUp.html')
def PsignUp(request):
    return render(request, 'PsignUp.html')
def createacc(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        staddr = request.POST.get('staddr')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')

        dob = request.POST.get('dob')
        gender = request.POST.get('gender')

        ssn = request.POST.get('ssn')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        insName = request.POST.get('insName')
        policyNum = request.POST.get('policyNum')

        username = request.POST.get('username')
        password = request.POST.get('password')

        profile = Profile.objects.create_user(username= username, email = email, password = password, ssn = ssn)
        profile.first_name = fname
        profile.last_name = lname

        profile.save()
        messages.success(request, "Your account has been successfully made!")
        return redirect('home')
    return render(request, 'PsignUp.html')

def createdocacc(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        staddr = request.POST.get('staddr')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')

        dob = request.POST.get('dob')
        gender = request.POST.get('gender')

        ssn = request.POST.get('ssn')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        doctor_id = request.POST.get('doctor_id')
        specialty = request.POST.get('specialty')

        username = request.POST.get('username')
        password = request.POST.get('password')

        profile = Profile.objects.create_user(username= username, email = email, password = password, ssn = ssn)
        profile.first_name = fname
        profile.last_name = lname
        profile.specialty = specialty

        profile.save()
        messages.success(request, "Your account has been successfully made!")
        return redirect('home')
    return render(request, 'DRsignUp.html')

def createappt(request):
    return render(request, 'CreateAppt.html')
def back(request):
    return render(request, 'PatientHomepage.html')



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


class ProfileDetailView(DetailView):
    model = Profile

    def my_view(request, id):
        my_object = Profile.objects.get(email__exact=id)
        return render(request, 'index.html', {'my_object': my_object})
    
