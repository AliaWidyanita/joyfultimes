from django.urls import path
from authentications.views import login_user
from authentications.views import register
from authentications.views import logout_user
app_name = 'authentications'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register') 
]