from django.shortcuts import render

def gallery(request):
    return render(request,'gallery.htmml')

def about(request):
    return render(request,'about.html')
