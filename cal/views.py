from datetime import datetime, timedelta, date
from urllib import request
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import calendar
from django.core import serializers

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

from .models import *
from .utils import Calendar
from .forms import EventForm

def index(request):
    return HttpResponse('hello')

# @login_required(login_url='/authentications/login')
class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month, self.request.user)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


@login_required(login_url='/authentications/login')
def event(request, event_id=None):
    # instance = Event()
    # if event_id:
    #     instance = get_object_or_404(Event, pk=event_id)
    # else:
    #     instance = Event()

    # form = EventForm(request.POST or None, instance=instance)
    # if request.POST and form.is_valid():
    #     form.save()
    #     return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html')
@login_required(login_url='/authentications/login')
@csrf_exempt
def event_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        range = request.POST['range']
        mood_new = Event(user=request.user, title=title, description=description, start_time=start_time, end_time=end_time, range=range)
        mood_new.save()
        mood= {'title': mood_new.title, 'description':mood_new.description, 'start_time':mood_new.start_time,'end_time':mood_new.end_time, 'range':mood_new.range}
        data={ 
            'mood':mood,
            'url': 'cal/calendar'}
    return JsonResponse(data)

@login_required(login_url='/authentications/login')
def event_edit(request, event_id):
    event = Event.objects.get(id=event_id)
    print(event.description, event.title)
    return render(request, 'cal/eventedit.html', { "event" : event})

@login_required(login_url='/authentications/login')
@csrf_exempt
def event_edit_post(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        event.title = request.POST['title']
        event.description = request.POST['description']
        event.start_time = request.POST['start_time']
        event.end_time = request.POST['end_time']
        event.range = request.POST['range']
        event.save()
        event_resp= {'title': event.title, 'description':event.description, 'start_time':event.start_time,'end_time':event.end_time, 'range':event.range}
        data={ 
            'mood':event_resp,
            'url': 'cal/calendar'}
    return JsonResponse(data)
@login_required(login_url='/authentications/login')
def showJsonMood(request):
    mood = Event.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('json', mood))
@csrf_exempt
@login_required(login_url='/authentications/login')
def event_post_free(request):
    if request.method == 'POST':
        store = json.loads(request.body.decode('utf-8'))
        print(store)
        title = store['title']
        description = store['description']
        start_time = store['start_time']
        end_time = store['end_time']
        range = store['range']
        user = request.user
        mood_new = Event(user=user,title=title, description=description, start_time=start_time, end_time=end_time, range=range)
        mood_new.save()
        mood= {'title': mood_new.title, 'description':mood_new.description, 'start_time':mood_new.start_time,'end_time':mood_new.end_time, 'range':mood_new.range, 'status': 'success'}
    else:
        mood= {'status': 'failed'}
    return JsonResponse(mood)

# def delete_all(request):
#     Event.objects.all().delete()
#     HttpResponse('cal/calendar')