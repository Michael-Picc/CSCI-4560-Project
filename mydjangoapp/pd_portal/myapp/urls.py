from django.urls import path, include
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

# These are the browser locations
urlpatterns = [
 path('med_loc/', Med_LocList.as_view()),
 path('med_loc/<int:pk>/', Med_LocDetail.as_view()),
 path('medical_history/', Medical_HistoryList.as_view()),
 path('medical_history/<int:pk>/', Medical_HistoryDetail.as_view()),
 path('doctor/', DoctorList.as_view()),
 path('doctor/<int:pk>/', DoctorDetail.as_view()),
 path('appointment/', AppointmentList.as_view()),
 path('appointment/<int:pk>/', AppointmentDetail.as_view()),
 path('patient/', PatientList.as_view()),
 path('patient/<int:pk>/', PatientDetail.as_view()),
 path('profile/', Profile, name='profile'),
path("index/", ProfileDetailView.as_view(), name="profile-detail"),
path('home', views.home,name = "home"),
path('loginfunc', views.loginfunc,name = "loginfunc"),
path('choice', views.choice,name = "choice"),
path('DRsignUp', views.DRsignUp,name = "DRsignUp"),
path('PsignUp', views.PsignUp,name = "PsignUp"),
path('createacc', views.createacc,name = "creatacc"),
path('createappt', views.createappt,name = "createappt"),
path('back', views.back,name = "back"),
path('createdocacc', views.createdocacc,name = "createdocacc"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
