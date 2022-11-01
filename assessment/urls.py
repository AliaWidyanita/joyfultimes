from django.urls import path
from .views import *

app_name = 'assessment'

urlpatterns = [
    path('', assessment, name='assessment'),

    path('depression-assessment/', depression_assessment, name='depression_assessment'),
    path('depression-assessment-json/', depression_assessment_json, name='depression_assessment_json'),
    path('fetch-depression-result/', add_depression_result, name='add_depression_result'),
    path('add-depression-result/', fetch_depression_result, name='fetch_depression_result'),

    path('anxiety-assessment/', anxiety_assessment, name='anxiety_assessment'),
    path('anxiety-assessment-json/', anxiety_assessment_json, name='anxiety_assessment_json'),
    path('fetch-anxiety-result/', add_anxiety_result, name='add_anxiety_result'),
    path('add-anxiety-result/', fetch_anxiety_result, name='fetch_anxiety_result'),
    
    path('stress-assessment/', stress_assessment, name='stress_assessment'),
    path('stress-assessment-json/', stress_assessment_json, name='stress_assessment_json'),
    path('fetch-stress-result/', add_stress_result, name='add_stress_result'),
    path('add-stress-result/', fetch_stress_result, name='fetch_stress_result'),
]