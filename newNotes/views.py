from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.
from newNotes.models import Notes
from newNotes.forms import addNotesForm
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
import random
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def get_notes(request):
    form = addNotesForm()
    users = get_user_model()
    allUsers = users.objects.all()
    data_notes = []
    for pengguna in allUsers:
        userNotes = Notes.objects.filter(user = pengguna)
        data_notes.append(userNotes)
    if data_notes:
        random_note = random.choice(data_notes)
    else:
        random_note = Notes.objects.all()
    
    context = {
            'list_notes' : random_note,
            'form' : form,
        }
    return render(request, 'newnotes_page.html', context)

def notes_json(request):
    data_notes = list(Notes.objects.all())
    if data_notes:
        randomizer = random.choice(data_notes)
        notes = serializers.serialize('json', [randomizer])
    else:
        notes = serializers.serialize('json', Notes.objects.all())
    return HttpResponse(notes, content_type="application/json")


@login_required(login_url='/authentications/login')
def create_notes(request):
    form = addNotesForm()
    
    if request.method == 'POST':
        form = addNotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()

    context = {
        'form' : form,
    }
    return render(request, 'newnotes_page.html', context)

@csrf_exempt
def add_notes_obj(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            sender = data['sender']
            title = data['title']
            notes = data['notes']

            newNote = Notes.objects.create(user = request.user , sender=sender, title=title, notes=notes)
            newNote.save()

            return JsonResponse({'status': 'success'})
        # user = request.user
        # sender = request.POST.get('sender')
        # title = request.POST.get('title')
        # notes = request.POST.get('notes')

        # Notes.objects.create(user=user, sender=sender, title=title,notes=notes)

        # return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})

@login_required(login_url='/authentications/login')
def delete_data(request):
    Notes.objects.all().delete()
    return HttpResponseRedirect(reverse('newNotes:get_notes'))

@login_required(login_url='/authentications/login')
def get_notes_all(request):
    data_notes = Notes.objects.filter(user=request.user)
    notes_size = data_notes.count()
    context = {
            'list_notes' : data_notes,
            'list_count' : notes_size,
        }
    return render(request, 'newnotes_userpage.html', context)

@login_required(login_url='/authentications/login')
def fetch_flutter(request):
    notes = Notes.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('json', notes))

@login_required(login_url='/authentications/login')
def notes_json_all(request):
    data = Notes.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json',data),content_type="application/json")

@login_required(login_url='/authentications/login')
def delete(request, id):
    item = Notes.objects.get(user = request.user, id=id)
    item.delete()
    return redirect('newNotes:get_notes_all')