from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import todo
from .forms import todoform

def index(request):
    tasks = todo.objects.all()
    form = todoform()

    if request.method == 'POST':
        form = todoform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks,'form':form}
    return render(request, "list.html",context)

def update_task(request, pk):

    task= todo.objects.get(id=pk)

    form = todoform(instance=task)

    if request.method=='POST':
        form = todoform(request.POST, instance=task)
        if form.is_valid():
            form.save() 
            return redirect('/')

    context = {'form':form}

    return render(request, 'update_task.html', context)

def delete(request, pk):
    item = todo.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect('/')

    context={'item': item}

    return render(request,'delete.html', context)