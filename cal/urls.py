from django.urls import include, path
from . import views

app_name = 'cal'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('calendar/',views.CalendarView.as_view(), name='calendar'),
    path('new/',views.event, name='event_new'),
    path('edit/<int:id>',views.event, name='event_edit'),

    ]