from django.urls import include, path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'cal'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('',login_required(views.CalendarView.as_view(), login_url='/authentications/login'), name='calendar'),
    path('event/new/',views.event, name='event_new'),
    path('event/edit/<int:event_id>',views.event_edit, name='event_edit'),
    path('event/new-post/',views.event_post, name='event_new_post'),
    path('event/new-post-free/',views.event_post_free, name='event_new_post_free'),
    path('event/edit-post/<int:event_id>',views.event_edit_post, name='event_edit_post'),
    path('event/json/',views.showJsonMood, name='showJsonMood'),
    # path('event-delete/',views.delete_all, name='delete_all'), @login_required(login_url='/authentications/login')
    ]