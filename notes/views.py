from ast import List
from email import contentmanager
from django.shortcuts import render
from notes.models import Notes
from notes.forms import addNotesForm
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
import random

# Create your views here.

def get_notes(request):
    form = addNotesForm()
    data_notes = list(Notes.objects.all())
    if data_notes:
        random_note = random.choice(data_notes)
    else:
        random_note = Notes.objects.all()
    
    context = {
            'list_notes' : random_note,
            'form' : form,
        }
    return render(request, 'notes_page.html', context)


def show_notes(request):
    if request.is_ajax():
        data_notes = list(Notes.objects.all())
        if data_notes:
            random_note = random.choice(data_notes)
        else:
            random_note = Notes.objects.all()
        notes_all = []
        for note in random_note:
            item = {
                'sender' : note.sender,
                'title' : note.title,
                'message' : note.notes
            }
            notes_all.append(item)
    return JsonResponse({'notes_all':notes_all})

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
            note.save()

    context = {
        'form' : form,
    }
    return render(request, 'notes_page.html', context)

@login_required(login_url='/authentications/login')
def delete_data(request):
    Notes.objects.all().delete()
    return HttpResponseRedirect(reverse('notes:get_notes'))

@login_required(login_url='/authentications/login')
def get_notes_all(request):
    form = addNotesForm()
    data_notes = Notes.objects.all()
    context = {
            'list_notes' : data_notes,
            'form' : form,
        }
    return render(request, 'notes_page.html', context)