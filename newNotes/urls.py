from django.urls import path 
from newNotes.views import get_notes,  notes_json,create_notes,delete_data,get_notes_all,notes_json_all,delete,add_notes_obj,fetch_flutter

app_name = 'newNotes'

urlpatterns = [
    path('', get_notes, name='get_notes'),
    path('json/', notes_json, name='notes_json'),
    path('fetch_flutter/', fetch_flutter, name='notes_flutter'),
    path('create/', create_notes, name='create_notes'),
    path('createfromflutter/',add_notes_obj, name='create_flutter'),
    path('all/', get_notes_all, name='get_notes_all'),
    path('alljson/',notes_json_all,name='notes_json_all'),
    path('all/delete/<int:id>/',delete,name='delete'),
    ]