from django.urls import path
from core.views import index, login_view, logout_view

urlpatterns = [
    path('', index, name="home"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]