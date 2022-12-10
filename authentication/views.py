from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.backends import UserModel
import json

# Create your views here.

@csrf_exempt
def flutter_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'username': username, 'login': True})
        else:
            return JsonResponse({'status': 'failed', 'login': False})

@csrf_exempt
def flutter_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 != password2:
            return JsonResponse({'status': 'failed', 'message': 'Gagal woi'})
        User.objects.create_user(username=username, password=password1, email=email)
        return JsonResponse({'status': 'success'})