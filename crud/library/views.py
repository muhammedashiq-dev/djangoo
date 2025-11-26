from django.shortcuts import render,redirect
from .forms import libraryform
from .models import librarydatabase
from django.core.paginator import Paginator

def create(request):
    if request.method == 'POST':
        form = libraryform(request.POST)
        if form.is_valid():
            lib = form.save()
            return redirect('create')
    else:
        form = libraryform()
    return render(request,'create.html',{'form':form})

def read(request):
    list = librarydatabase.objects.all()
    return render(request,'data.html',{
        'list' : list
    })  
    
def update(request,id):
     lib = librarydatabase.objects.get(pk = id)
     if request.method == 'POST':
        form = libraryform(request.POST,instance=lib)
        if form.is_valid():
            form.save()
            return redirect('read')
     else:
         form = libraryform(instance = lib)
         return render(request,'update.html',{
             'form':form
         })
         
def delete(request,id):
    lib = librarydatabase.objects.get(pk = id)
    if request.method == 'POST':
        lib.delete()
        return redirect('read')
    
    return render(request,'delete.html',{'lib':lib})

def list(request):
    liblist =librarydatabase.objects.all()
    paginator = Paginator(liblist,5)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request,'list.html',{
        'page_obj':page_obj
    })