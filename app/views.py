from django.shortcuts import render
from django.http import HttpResponse
from app.models import multipleSearchFields

def SearchViews(request):
    if request.method=='POST':
        occapation = request.POST.get('occapation')
        gender = request.POST.get('gender')
        searchQuery = multipleSearchFields.objects.filter(occapation__icontains=occapation,gender__icontains=gender)
        return render(request,'index.html',{'all_obj':searchQuery})
    else:
        all_obj = multipleSearchFields.objects.all()
        return render(request,'index.html',{'all_obj':all_obj})
    

