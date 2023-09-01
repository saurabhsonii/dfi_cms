from django.contrib import admin
from .models import CustomUser, Contact, VehicleDetails, PersonalDetails, State

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Contact)
admin.site.register(VehicleDetails)
admin.site.register(PersonalDetails)
admin.site.register(State)
