from django.contrib import admin

from django.contrib import admin
from .models import Staff, Office,Darbandi, Post, Address, Family, Appointment,  DesiredPerson,  Service, EducationalInfo, LeaveInfo, PunishmentInfo, Treatment


@admin.register(Staff, Office,Darbandi, Post, Address, Family, Appointment,  DesiredPerson,  Service, EducationalInfo, LeaveInfo, PunishmentInfo, Treatment
)
class PersonAdmin(admin.ModelAdmin):
    pass
