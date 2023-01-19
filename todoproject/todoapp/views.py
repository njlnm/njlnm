from django.shortcuts import render
from .models import Task

# Create your views here.

def index(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        task=Task(name=name,priority=priority)
        task.save()

    return render(request,'home.html',{'task1':task1})


#def details(request):

   # return render(request,'detail.html',)
