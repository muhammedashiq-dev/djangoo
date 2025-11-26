from django.shortcuts import render
from .forms import libraryform

def greeting(request):
    if request.method == 'POST':
        form = libraryform(request.POST)
        if form.is_valid():
            lib = form.save()
            return render(request, 'library/data.html', {'library': lib})
    else:
        form = libraryform()

    return render(request, 'library/home.html', {'form': form})
