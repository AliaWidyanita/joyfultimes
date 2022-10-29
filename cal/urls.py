from django.urls import include, path
from . import views

app_name = 'cal'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('',views.CalendarView.as_view(), name='calendar'),
    path('event/new/',views.event, name='event_new'),
    path('event/edit/<int:event_id>',views.event_edit, name='event_edit'),
    path('event/new-post/',views.event_post, name='event_new_post'),
    path('event/edit-post/<int:event_id>',views.event_edit_post, name='event_edit_post'),
    ]