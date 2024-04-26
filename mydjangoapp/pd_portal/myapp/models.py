from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _




states = {"Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

class Profile(AbstractUser):
    date_added = models.DateField(auto_now_add=True)
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(_('email address'), unique = True)
    phone_no = models.CharField(max_length = 10)
    USERNAME_FIELD = 'email'
    ssn = models.IntegerField(unique=True,blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=40, choices=states)
    zip = models.IntegerField(blank=True,null=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name','ssn','address']
    email_isauth = models.BooleanField(default=False)
    DOB = models.DateField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=200)
    def __str__(self):
        return "{}".format(self.email)
    
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

class Doc_Profile(Profile):
    stationed = models.ForeignKey(Med_Loc, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=50)
    patients = models.JSONField()
    def __str__(self):
        return self.first_name+' '+self.last_name
    
class Pat_Profile(Profile):
    bill_address = models.CharField(max_length=100, default='0')
    def __str__(self):
        return self.first_name+' '+self.last_name

class Appointment(models.Model):
    day = models.DateField()
    time = models.TimeField()
    reason = models.CharField(max_length=500)
    id = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    d = models.ForeignKey(Doc_Profile, on_delete=models.PROTECT)
    p = models.ForeignKey(Pat_Profile, on_delete=models.PROTECT)
    status = models.BooleanField()
    
    def __str__(self):
        return self.id

class Medical_History(models.Model):
    p = models.ForeignKey(Pat_Profile, on_delete=models.PROTECT)
    d = models.ForeignKey(Doc_Profile, on_delete=models.PROTECT)
    doctor_notes = models.TextField(max_length=500)
    meds = models.JSONField()
    allergies = models.JSONField()
    appointments = models.ForeignKey(Appointment, on_delete=models.PROTECT)
    id = models.IntegerField(auto_created=True,unique=True,primary_key=True)

    def __str__(self):
        return self.id