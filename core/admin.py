from django.contrib import admin
from .models import (CustomUser, Contact, VehicleDetails, PersonalDetails, State,
                     OccupationDetails, DocumentImages, VehicleDocuments, Disbursement)
from django.contrib.admin import TabularInline
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Contact)
# admin.site.register(VehicleDetails)
admin.site.register(PersonalDetails)
admin.site.register(State)
admin.site.register(OccupationDetails)
# admin.site.register(DocumentImages)
admin.site.register(VehicleDocuments)
admin.site.register(Disbursement)


# @admin.register(DocumentImages)


@admin.register(VehicleDetails)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ("vehicle_name", "vehicle_model", "created_at")
    list_filter = ("vehicle_name",)
    search_fields = ('vehicle_name', 'vehicle_model')
