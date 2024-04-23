# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import *

admin.site.register(Med_Loc)
admin.site.register(Medical_History)
admin.site.register(Doc_Profile)
admin.site.register(Appointment)
admin.site.register(Pat_Profile)
admin.site.register(Profile)