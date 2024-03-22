from django.db import models


class Med_Loc(models.Model):
    #type of medical center
    DESIGNATIONS = {
        'H': 'Hospital',
        'D': 'Drug Store',
        'C': 'Clinic',
    }
    med_type = models.CharField(max_length=1, choices=DESIGNATIONS)
    #primary key
    id = models.IntegerField(auto_created=True,unique=True,primary_key=True)
    # location
    street_num = models.IntegerField()
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.IntegerField()
    location = str(street_num)+' '+str(street_name)+', '+str(city)+' '+str(zip)
    med_name = models.CharField(max_length=50)


    def __str__(self):
        return self.med_name
    
class Health_Insurance(models.Model):
    name = models.CharField(max_length=75)
    id = models.IntegerField(auto_created=True,unique=True,primary_key=True)
    policy = models.JSONField()

    def __str__(self):
        return self.id
    
    

    
class Doctor(models.Model):
    stationed = models.ForeignKey(Med_Loc, on_delete=models.CASCADE)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    patients = models.JSONField()
    SSN = models.IntegerField(unique=True,primary_key=True)

    def __str__(self):
        return self.fName+' '+self.lName
    

class Patient(models.Model):
    date_added = models.DateField(auto_now_add=True)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    DOB = models.DateField()
    SSN = models.IntegerField(unique=True, primary_key=True)
    patientLocation = models.CharField(max_length=100)
    health_insurance = models.ForeignKey(Health_Insurance, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    street_num = models.IntegerField()
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.IntegerField()
    bill = models.FloatField()
    #med_history = models.ForeignKey(Medical_History)

    def __str__(self):
        return self.fName+' '+self.lName

class Appointment(models.Model):
    day = models.DateField()
    time = models.TimeField()
    reason = models.CharField(max_length=500)
    id = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    d_id = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    p_id = models.ForeignKey(Patient, on_delete=models.PROTECT)
    status = models.BooleanField()
    
    def __str__(self):
        return self.id

class Medical_History(models.Model):
    p_id = models.ForeignKey(Patient, on_delete=models.PROTECT)
    d_id = models.ForeignKey(Doctor,on_delete= models.PROTECT)
    doctor_notes = models.CharField(max_length=500)
    meds = models.JSONField()
    allergies = models.JSONField()
    appointments = models.ForeignKey(Appointment, on_delete=models.PROTECT)
    id = models.IntegerField(auto_created=True,unique=True,primary_key=True)

    def __str__(self):
        return self.id




    

    

    

