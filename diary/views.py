from django.shortcuts import render, redirect
from diary.forms import AddDiaryForm
from diary.models import Diary
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime

# Create your views here
@login_required(login_url='/authentications/login')
def show_diary(request):
    diary_items = Diary.objects.filter(user = request.user)
    context = {
        'username': request.user.username,
        'diary_items': diary_items,
    }
    return render(request, 'diary_home.html', context)

def show_detail(request, id):
    the_item = Diary.objects.filter(user = request.user, id=id)
    context = {"item": serializers.serialize("json", the_item)}
    return render(request, 'detail.html', context)

@login_required(login_url='authentications/login/')
def page_add(request):
    form = AddDiaryForm()
    context = {'form': form,'username': request.user.username,}
    if request.method == 'POST':
        form = AddDiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()
            return redirect('diary:show_diary')
    return render(request, 'create.html', context)

def json_diary(request):
    diary = Diary.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('json', diary))

def add_diary(request):
    form = AddDiaryForm()
    if request.method == 'POST':
        form = AddDiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()
            return HttpResponse(diary)

        return HttpResponseBadRequest("Hmm.. What's wrong?")

def update(request, id):
    item = Diary.objects.filter(user = request.user, id = id)
    context = {'id': item[0].id, 'title': item[0].title, 'body': item[0].body}
    return render(request, 'update.html', context)

def updaterecord(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        item = Diary.objects.get(user = request.user, id=id)
        item.title = title
        item.body = body
        item.save()
        return redirect('diary:show_detail', id=item.id)
    return HttpResponseBadRequest("Hmm.. What's wrong?")

def delete(request, id):
    item = Diary.objects.get(user = request.user, id = id)
    item.delete()
    return redirect('diary:show_diary')
    