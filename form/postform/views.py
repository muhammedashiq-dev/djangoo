from django.shortcuts import render
def user_pdetails(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        return render(request,'post_data.html',{
            'postdata' : request.POST,
            'name' : name,
            'color': color
        })
    return render(request,'post.html')
        
