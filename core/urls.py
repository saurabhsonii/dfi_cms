from django.urls import path
from core.views import index, login_view

urlpatterns = [
    path('', index_view, name="home"),
    path('login/', login_view, name='login'),
]