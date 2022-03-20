from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.


def index(request):
    return render(request, 'main/index.html', {"Title": "The main page of the site"})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = "no errors"
    # if request.method() == "POST"
    if 1:
        form2 = TaskForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('todo')
        else:
            error = "form is invalid"
    form = TaskForm()
    return render(request, 'main/create.html',  {'Title': "Creation page",'form': form, 'error': error})


def todo(request):
    tasks = Task.objects.all()
    return render(request, 'main/todo.html', {"Title": "Todo", "tasks": tasks})


def lolkek(request):
    return render(request, 'main/lolkek.html', {'Title': "lol"})


def chess(request):
    return render(request, 'main/chess.html')


def pricelist(request):
    return render(request, 'main/pricelist.html')


def statistics(request):
    return render(request, 'main/statistics.html')
