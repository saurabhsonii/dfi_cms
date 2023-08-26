from django.urls import path
from core.views import index_view, login_view, contact_view, logout_view, contact_list, contact_details, delete_contact

urlpatterns = [
    path('', index_view, name="home"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contact/', contact_view, name='contact'),
    path('contact-list/', contact_list, name='contact_list'),
    path('contacts/<int:contact_id>/', contact_details, name='contact_details'),
    path('contacts/<int:contact_id>/delete/',
         delete_contact, name='delete_contact'),

]
