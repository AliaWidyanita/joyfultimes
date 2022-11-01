from django.urls import path 
from newNotes.views import get_notes,  notes_json,create_notes,delete_data,get_notes_all,notes_json_all
app_name = 'newNotes'

urlpatterns = [
    path('', get_notes, name='get_notes'),
    path('json/', notes_json, name='notes_json'),
    path('create/', create_notes, name='create_notes'),
    path('delete/',delete_data, name='delete_data'),
    path('all/', get_notes_all, name='get_notes_all'),
    path('alljson/',notes_json_all,name='notes_json_all')
    ]