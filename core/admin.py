from django.contrib import admin
from .models import (CustomUser, Contact, LoanDetails, PersonalDetails, State,
                     OccupationDetails, DocumentImages, VehicleDocuments, Disbursement)

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Contact)
admin.site.register(LoanDetails)
admin.site.register(PersonalDetails)
admin.site.register(State)
admin.site.register(OccupationDetails)
admin.site.register(DocumentImages)
admin.site.register(VehicleDocuments)
admin.site.register(Disbursement)
