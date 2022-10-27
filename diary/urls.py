from django.urls import path
from diary.views import show_diary, json_diary, json_detail, add_diary, page_add, show_detail

app_name = 'diary'

urlpatterns = [
    path('', show_diary, name='show_diary'),
    path('json/', json_diary, name='json_diary'),
    path('json/<int:id>', json_detail, name='json_detail'),
    path('add/', add_diary, name='add_diary'), 
    path('create/', page_add, name='page_add'),
    path('<int:id>/', show_detail, name='show_detail'),
]