from django.shortcuts import render
from .forms import contactform
from .models import contactinfo
def con(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            pers = contactinfo()
            pers.full_name = form.cleaned_data['full_name']
            pers.email = form.cleaned_data['email']
            pers.phone_number = form.cleaned_data['phone_number']
            pers.save()
            return render(request,'data.html',{
                 'message': 'Data saved to db',
                 'full_name' : pers.full_name
            })
    else:
        form = contactform()
    return render(request,'movie.html',{'form':form})