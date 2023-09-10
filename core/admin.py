from django.contrib import admin
from .models import (CustomUser, Contact, LoanDetails, PersonalDetails,
                     OccupationDetails, DocumentImages, VehicleDocuments, Disbursement, PatternSourcing, ChannalPattern)
from django.contrib.admin import TabularInline
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Contact)
admin.site.register(PatternSourcing)
# admin.site.register(PatternSourcing)
admin.site.register(ChannalPattern)
admin.site.register(OccupationDetails)
admin.site.register(DocumentImages)
admin.site.register(VehicleDocuments)
admin.site.register(Disbursement)


# @admin.register(DocumentImages)


@admin.register(LoanDetails)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ("vehicle_name", "vehicle_model", "created_at")
    list_filter = ("vehicle_name",)
    search_fields = ('vehicle_name', 'vehicle_model')
