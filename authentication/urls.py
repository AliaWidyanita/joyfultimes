from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login_flutter/', login, name='login')
]