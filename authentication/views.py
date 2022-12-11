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
        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": "duplicate"}, status=401)

        if password1 != password2:
            return JsonResponse({"status": "pass failed"}, status=401)
        User.objects.create_user(username=username, password=password1)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({"status": "error"}, status=401)

def get_data(request):

    return JsonResponse({
        "username":request.user.username
    })