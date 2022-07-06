from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.http import JsonResponse
from .models import StudentDetails,District,State
from django.core import serializers

def home(request):
    return render(request,"home.html")

def addStudent(request):
    if request.method == "POST":
        
        image=request.FILES['image']
        stduent=StudentDetails.objects.create(fullName=request.POST.get("FullName"),phoneNumber=request.POST.get("phoneNumber"),email=request.POST.get("email"),
                    state=request.POST.get("State"),district=request.POST.get("District"),image=image)
        stduent.save()
        

    states=State.objects.all()
    

    return render(request,"studentForm.html",{"state":states})

def viewstudents(request):
    students=StudentDetails.objects.all()
    return render(request,"students.html",{'students':students})


def getdistrict(request):
    district=list(District.objects.filter(state_id=request.GET.get('state')).values_list("district",flat=True)) 

    return JsonResponse({'success': True, 'district': district})

def student(request,id):
    stud=StudentDetails.objects.get(stdcode=id)
    return render(request,"viewstudent.html",{"student":stud})