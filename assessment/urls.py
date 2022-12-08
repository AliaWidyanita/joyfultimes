from django.urls import path
from .views import *

app_name = 'assessment'

urlpatterns = [
    path('', assessment, name='assessment'),

    path('depression-assessment/', depression_assessment, name='depression_assessment'),
    path('depression-assessment-json/', depression_assessment_json, name='depression_assessment_json'),
    path('fetch-depression-result-flutter/', fetch_depression_result_flutter, name='fetch_depression_result_flutter'),
    path('add-depression-result-flutter/', add_depression_result_flutter, name='add_depression_result_flutter'),

    path('anxiety-assessment/', anxiety_assessment, name='anxiety_assessment'),
    path('anxiety-assessment-json/', anxiety_assessment_json, name='anxiety_assessment_json'),
    path('fetch-anxiety-result-flutter/', fetch_anxiety_result_flutter, name='fetch_anxiety_result_flutter'),
    path('add-anxiety-result-flutter/', add_anxiety_result_flutter, name='add_anxiety_result_flutter'),
    
    path('stress-assessment/', stress_assessment, name='stress_assessment'),
    path('stress-assessment-json/', stress_assessment_json, name='stress_assessment_json'),
    path('fetch-stress-result-flutter/', fetch_stress_result_flutter, name='fetch_stress_result_flutter'),
    path('add-stress-result-flutter/', add_stress_result_flutter, name='add_stress_result_flutter'),
]