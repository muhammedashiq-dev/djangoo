from django.shortcuts import render
from .forms import Loginform

def validate(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            return render(request, 'validate.html', {
                'email': form.cleaned_data['email']
            })
        else:
            return render(request, 'index.html', {'form': form})

    return render(request, 'index.html', {'form': Loginform()})
