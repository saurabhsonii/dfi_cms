from django.urls import path
from core.views import index_view, login_view, contact_view, logout_view, contact_list, contact_details, delete_contact, register_agent, agent_list, update_agent

urlpatterns = [
    path('', index_view, name="home"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contact/', contact_view, name='contact'),
    path('contact-list/', contact_list, name='contact_list'),
    path('contacts/<int:contact_id>/', contact_details, name='contact_details'),
    path('contacts/<int:contact_id>/delete/',
         delete_contact, name='delete_contact'),
    path('register-agent/', register_agent, name='register_agent'),
    path('agent-list/', agent_list, name='agent_list'),
    path('update-agent/<int:agent_id>/', update_agent, name='update_agent'),

]
