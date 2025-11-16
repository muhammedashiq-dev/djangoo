from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            return render(request, 'success.html', {'name': full_name})
        else:
            return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': RegistrationForm()})
