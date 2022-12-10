import json
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Function for render main, html, and display quiz object
def assessment(request):
    assessment = MentalHealthAssessment.objects.all()
    context = {'quizs' : assessment}
    return render(request, 'main.html', context)

# Function for depression assessment
def depression_assessment(request):
    form = DepressionTest()

    if request.user.is_authenticated:
        hasil_assessment = MentalHealthAssessment.objects.filter(user=request.user, topic=1).first()
    else:
        hasil_assessment = None

    context = {'form': form, 'hasil_assessment': hasil_assessment, 'name': 'Depression Assessment', 'url': 'depression'}
    return render(request, 'quiz.html', context)

# Function for calculationg depression assessment score for user
def depression_assessment_json(request):
    if request.method == 'POST':
        form = DepressionTest(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            skor = int(form_data['phq_1']) + int(form_data['phq_2']) + int(form_data['phq_3']) + int(form_data['phq_4']) + int(form_data['phq_5']) + int(
                form_data['phq_6']) + int(form_data['phq_7']) + int(form_data['phq_8']) + int(form_data['phq_9']) + int(form_data['phq_10'])

            if skor >= 20:
                result = "High Depression Level"
            elif skor >= 15:
                result = "Moderate Depression Level"
            elif skor >= 10:
                result = "Mild Depression Level"
            elif skor >= 5:
                result = "Little Depression Level"
            else:
                result = "No Depression"

            if request.user.is_authenticated:
                hasil_assessment = MentalHealthAssessment.objects.filter(user=request.user, topic=1).first()
                if hasil_assessment:
                    hasil_assessment.result = result
                    hasil_assessment.save()
                else:
                    hasil_assessment = MentalHealthAssessment(user=request.user, topic=1, result=result)
                    hasil_assessment.save()
            return JsonResponse({'result': result})
        else:
            return JsonResponse({'error': form.errors})
    return redirect('assessment:depression_assessment')

@csrf_exempt
def add_depression_result_flutter(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            result = data["result"]
            
            hasil_assessment = MentalHealthAssessment.objects.filter(user=request.user, topic=1).first()
            if hasil_assessment:
                hasil_assessment.result = result
                hasil_assessment.save()
            else:
                hasil_assessment = MentalHealthAssessment(user=request.user, topic=1, result=result)
                hasil_assessment.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def fetch_depression_result_flutter(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            hasil_assessment = MentalHealthAssessment.objects.filter(user=request.user, topic=1).first()
            if hasil_assessment:
                return JsonResponse({"result": hasil_assessment.result, "date": hasil_assessment.date}, status=200)
        return JsonResponse({"result": "", "date": ""}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

# Function for anxiety assessment
def anxiety_assessment(request):
    form = AnxietyTest()

    if request.user.is_authenticated:
        hasil_assessment = MentalHealthAssessment.objects.filter(user=request.user, topic=2).first()
    else:
        hasil_assessment = None

    context = {'form': form, 'hasil_assessment': hasil_assessment, 'name': 'Anxiety Assessment', 'url': 'anxiety'}
    return render(request, 'quiz.html', context)

# Function for calculationg anxiety assessment score for user
def anxiety_assessment_json(request):
    if request.method == 'POST':
        form = AnxietyTest(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            skor = int(form_data['phq_1']) + int(form_data['phq_2']) + int(form_data['phq_3']) + int(form_data['phq_4']) + int(form_data['phq_5']) + int(
                form_data['phq_6']) + int(form_data['phq_7']) + int(form_data['phq_8']) + int(form_data['phq_9']) + int(form_data['phq_10'])

            if skor >= 20:
                result = "High Anxiety Level"
            elif skor >= 15:
                result = "Moderate Anxiety Level"
            elif skor >= 10:
                result = "Mild Anxiety Level"
            elif skor >= 5:
                result = "Little Anxiety Level"
            else:
                result = "No Anxiety"

            if request.user.is_authenticated:
                hasil_assessment = MentalHealthAssessment.objects.filter(user=request.user, topic=2).first()
                if hasil_assessment:
                    hasil_assessment.result = result
                    hasil_assessment.save()
                else:
                    hasil_assessment = MentalHealthAssessment(user=request.user, topic=2, result=result)
                    hasil_assessment.save()
            return JsonResponse({'result': result})
        else:
            return JsonResponse({'error': form.errors})
    return redirect('assessment:anxiety_assessment')

@csrf_exempt
def add_anxiety_result_flutter(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            result = data["result"]
            
            hasil_assessment = MentalHealthAssessment.objects.filter(user=request.user, topic=2).first()
            if hasil_assessment:
                hasil_assessment.result = result
                hasil_assessment.save()
            else:
                hasil_assessment = MentalHealthAssessment(user=request.user, topic=2, result=result)
                hasil_assessment.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def fetch_anxiety_result_flutter(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            hasil_assessment = MentalHealthAssessment.objects.filter(user=request.user, topic=2).first()
            if hasil_assessment:
                return JsonResponse({"result": hasil_assessment.result, "date": hasil_assessment.date}, status=200)
        return JsonResponse({"result": "", "date": ""}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

# Function for stress assessment
def stress_assessment(request):
    form = StressTest()

    if request.user.is_authenticated:
        hasil_assessment = MentalHealthAssessment.objects.filter(user=request.user, topic=3).first()
    else:
        hasil_assessment = None

    context = {'form': form, 'hasil_assessment': hasil_assessment, 'name': 'Stress Assessment', 'url': 'stress'}
    return render(request, 'quiz.html', context)

# Function for calculationg stress assessment score for user
def stress_assessment_json(request):
    if request.method == 'POST':
        form = StressTest(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            skor = int(form_data['phq_1']) + int(form_data['phq_2']) + int(form_data['phq_3']) + int(form_data['phq_4']) + int(form_data['phq_5']) + int(
                form_data['phq_6']) + int(form_data['phq_7']) + int(form_data['phq_8']) + int(form_data['phq_9']) + int(form_data['phq_10'])

            if skor >= 20:
                result = "High Stress Level"
            elif skor >= 15:
                result = "Moderate Stress Level"
            elif skor >= 10:
                result = "Mild Stress Level"
            elif skor >= 5:
                result = "Little Stress Level"
            else:
                result = "No Stress"

            if request.user.is_authenticated:
                hasil_assessment = MentalHealthAssessment.objects.filter(user=request.user, topic=3).first()
                if hasil_assessment:
                    hasil_assessment.result = result
                    hasil_assessment.save()
                else:
                    hasil_assessment = MentalHealthAssessment(user=request.user, topic=3, result=result)
                    hasil_assessment.save()
            return JsonResponse({'result': result})
        else:
            return JsonResponse({'error': form.errors})
    return redirect('assessment:stress_assessment')

@csrf_exempt
def add_stress_result_flutter(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            result = data["result"]
            
            hasil_assessment = MentalHealthAssessment.objects.filter(user=request.user, topic=3).first()
            if hasil_assessment:
                hasil_assessment.result = result
                hasil_assessment.save()
            else:
                hasil_assessment = MentalHealthAssessment(user=request.user, topic=3, result=result)
                hasil_assessment.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def fetch_stress_result_flutter(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            hasil_assessment = MentalHealthAssessment.objects.filter(user=request.user, topic=3).first()
            if hasil_assessment:
                return JsonResponse({"result": hasil_assessment.result, "date": hasil_assessment.date}, status=200)
        return JsonResponse({"result": "", "date": ""}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)