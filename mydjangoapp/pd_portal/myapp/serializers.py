from rest_framework import serializers
from .models import *


class Med_LocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Med_Loc
        fields = ('__all__')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc_Profile
        fields = ('__all__')


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pat_Profile
        fields = ('__all__')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('__all__')

class Medical_HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical_History
        fields = ('__all__')
