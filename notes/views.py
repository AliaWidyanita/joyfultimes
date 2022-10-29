from django.shortcuts import render
from .models import Notes
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def get_notes(request):
    data_notes = Notes.objects.all()
    context = {
        'list_notes' : data_notes,
    }
    return render(request, 'notes_page.html', context)

def show_notes(request):
    if request.is_ajax():
        notes = Notes.objects.all()
        notes_all = []
        for note in notes:
            item = {
                'sender' : note.sender,
                'title' : note.title,
                'message' : note.notes
            }
            notes_all.append(item)
    return JsonResponse({'notes_all':notes_all})

def notes_json(request):
    notes = serializers.serialize('json', Notes.objects.all())
    return HttpResponse(notes, content_type="application/json")

@login_required(login_url='/authentications/login')
def create_notes(request):
    if request.method == 'POST':
        new = Notes.objects.create(sender=request.POST.get('sender'),title=request.POST.get('title'),notes=request.POST.get('message'))
        note = {
            'sender' : new.sender,
            'title' : new.title,
            'message' : new.message,
        }

        return JsonResponse(note)


def delete_data(request):
    Notes.objects.all().delete()
    return HttpResponseRedirect(reverse('notes:get_notes'))