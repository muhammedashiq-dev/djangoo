from django.shortcuts import render
def user_details(request):
    if request.method == 'GET' and 'username' in request.GET:
        username = request.GET.get('username')
        return render(request,'user_data.html',{
            'userdata' : request.GET,
            'username' : username
        })
    return render(request,'user.html')
        
