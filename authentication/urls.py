from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('loginFlutter/', flutter_login, name='login-flutter'),
    path('registerFlutter/', flutter_register, name='register-flutter'),
    path('data/', get_data, name="get_data")
]  