from django.shortcuts import render,HttpResponse

# Create your views here.
from .models import Education,Experience,PersonalDetails,Skills,Awards_recognitions,Certifications

def resume(request):
    personal_info = PersonalDetails.objects.first()
    skills = Skills.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    awards = Awards_recognitions.objects.all()

    context = {
        'personal_info':personal_info,
        'skills':skills,
        'education':education,
        'experience':experience,
        'awards':awards,
    }
    return render(request,'res_app/resume.html',context)

def home(request):
    return HttpResponse("<h1>Welcome to the My Resume</h1><p>Go to <a href='/res_app/resume/'>Show Resume</a></p>")
