from django.shortcuts import render,redirect
from django.http import HttpResponse
from skill.models import *
from django.http import JsonResponse
# Create your views here.
def home(request):
    return HttpResponse("hey hello")

def skill_list(request):
    skills = Skillmatrix.objects.all().order_by('user__username').distinct('user__username')
    print(skills.values())
    context={'skill':skills}
    print(context)
    return render(request,'home.html',context)

def skill_create(request):
    if request.method=='POST':
        user=request.POST.get['user']
        skill_name=request.POST.get['name']
        skill_level=request.POST.get['level']
        try:
            skill=Skillmatrix.objects.create(user=user,skill=skill_name,level=skill_level)
        except:
            return JsonResponse({'status':"data error while creating objects"})
        return redirect('home')
    return render(request,'home.html')