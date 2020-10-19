from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.

#takes the input of tasks and returns them, if any
def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all 
            messages.success(request , ("Task has been added to list!"))
            return redirect('index') #render(request, "todo/index.html", {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, "todo/index.html", {'all_items': all_items})

#delete a task
def delete(request, list_id):
    item = List.objects.get(pk= list_id)
    item.delete()
    messages.success(request, ("Task has been removed from list!"))
    return redirect('index')

#marking task as done
def cross_off(request, list_id):
    item = List.objects.get(pk= list_id)
    item.completed = True
    item.save()
    return redirect('index')

#marking a task as undone
def uncross(request, list_id):
    item = List.objects.get(pk= list_id)
    item.completed = False
    item.save()
    return redirect('index')

#editing task by clicking on the task
def edit(request, list_id):
    if request.method == "POST":
        item = List.objects.get(pk= list_id)

        form = ListForm(request.POST or None, instance= item)

        if form.is_valid():
            form.save()
            all_items = List.objects.all 
            messages.success(request, ("Task has been edited successfully!"))
            return redirect('index')
        
    else:
        item = List.objects.get(pk= list_id)
        return render(request, 'todo/edit.html', {'item': item})

//random comment


    

