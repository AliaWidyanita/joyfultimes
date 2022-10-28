from django.urls import path
from diary.views import show_diary, json_diary, add_diary, page_add, show_detail, update, updaterecord, delete

app_name = 'diary'

urlpatterns = [
    path('', show_diary, name='show_diary'),
    path('json/', json_diary, name='json_diary'),
    path('add/', add_diary, name='add_diary'), 
    path('create/', page_add, name='page_add'),
    path('<int:id>/', show_detail, name='show_detail'),
    path('update/<int:id>', update, name='update'),
    path('update/updaterecord/<int:id>', updaterecord, name='updaterecord'),
    path('delete/<int:id>', delete, name='delete'),

]