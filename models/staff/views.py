from django.shortcuts import render
from .forms import customerform
def greeting(request):
    if request.method == 'POST':
        form = customerform(request.POST)
        if form.is_valid():
            cust = form.save()
            return render (request,'data.html',{
                'message':'message saved to db'
            })
    else:
        form = customerform()
    return render(request,'customer.html',{'form':form})
