from django.urls import path
from .views import *

app_name = 'assessment'

urlpatterns = [
    path('', assessment, name='assessment'),

    path('depression-assessment/', depression_assessment, name='depression_assessment'),
    path('depression-assessment-json/', depression_assessment_json, name='depression_assessment_json'),

    path('anxiety-assessment/', anxiety_assessment, name='anxiety_assessment'),
    path('anxiety-assessment-json/', anxiety_assessment_json, name='anxiety_assessment_json'),
    
    path('stress-assessment/', stress_assessment, name='stress_assessment'),
    path('stress-assessment-json/', stress_assessment_json, name='stress_assessment_json'),
]