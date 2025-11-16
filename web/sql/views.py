from django.shortcuts import render
from .forms import movieregistration
from .models import moviedb
def list(request):
    if request.method == 'POST':
        form = movieregistration(request.POST)
        if form.is_valid():
            cust = moviedb()
            cust.movie_name = form.cleaned_data['movie_name']
            cust.release_year = form.cleaned_data['release_year']
            cust.save()
            return render(request,'data.html',{
                 'message': 'Data saved to db'
            })
    else:
        form = movieregistration()
    return render(request,'movie.html',{'form':form})