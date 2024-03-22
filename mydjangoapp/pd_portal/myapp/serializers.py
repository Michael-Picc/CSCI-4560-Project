from rest_framework import serializers
from .models import *


def create(self, validated_data,obj):
    # Once the request data has been validated, we can create a todo item instance in the database
    return obj.objects.create(
      text=validated_data.get('text')
    )

def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
    instance.text = validated_data.get('text', instance.text)
    instance.save()
    return instance

class Med_LocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Med_Loc
        fields = ('__all__')

class HealthInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_Insurance
        fields = ('__all__')
        
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('__all__')


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('__all__')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('__all__')

class Medical_HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical_History
        fields = ('__all__')
