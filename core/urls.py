from django.urls import path
from core.views import (index_view, login_view, contact_view, logout_view,
                        contact_list, contact_details, delete_contact, register_agent,
                        agent_list, update_agent)
# from core.views import MyWizardView
from .forms import PersonalDetailsForm, LoanDetailsForm, OccupationDetailsForm
from core import views

urlpatterns = [
    path('', index_view, name="home"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # ---------------------------------------------------------------------------
    path('contact/', contact_view, name='contact'),
    path('contact-list/', contact_list, name='contact_list'),
    path('contacts/<int:contact_id>/', contact_details, name='contact_details'),
    path('contacts/<int:contact_id>/delete/',
         delete_contact, name='delete_contact'),
    # ----------------------------------------------------------------------------
    path('register-agent/', register_agent, name='register_agent'),
    path('agent-list/', agent_list, name='agent_list'),
    path('update-agent/<int:agent_id>/', update_agent, name='update_agent'),

    # vehicle--------------------------------------------------------------------

    path('vehicle-details/', views.vehicle_details, name='vehicle_details'),
    
    path('home-details/', views.home_details, name='home_details'),
    path('business-details/', views.business_details, name='business_details'),
    path('micro-details/', views.micro_details, name='micro_details'),
    path('gold-details/', views.gold_details, name='gold_details'),

    path('personal-details/', views.personal_details, name='personal_details'),
    path('occupation_details/', views.occupation_details,
         name='occupation_details'),
    path('vehicle_documents/', views.vehicle_documents, name='vehicle_documents'),
    path('disbursement/', views.disbursement, name='disbursement'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('applicants/', views.ApplicantView, name='applicants'),
    path('edit_vehicle/<int:vehicle_id>/', views.edit_vehicle,
         name='edit_vehicle'),  # Add this line
    path('generate_loan_details_docx/<int:vehicle_id>/', views.generate_loan_details_docx,
         name='generate_loan_details_docx'),  # Add this line









]
