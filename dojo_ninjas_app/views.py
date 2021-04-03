from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        'all_dojos': Dojo.objects.all(),
    }
    
    return render(request, 'index.html', context)

def add_dojo(request):
    if request.method == 'POST':
        Dojo.objects.create(
            name=request.POST['name'], 
            city=request.POST['city'], 
            state=request.POST['state']
        )
    return redirect('/dojo_ninjas/')

def add_ninja(request):
    if request.method == 'POST':
        Ninja.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            dojo_id=request.POST['dojo']
        )
    return redirect('/dojo_ninjas/')

# def delete_dojo(request):