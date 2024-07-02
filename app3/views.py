from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def US(request):
    return HttpResponse("Lost the match") 

def test3(request):
    return render(request,'test3.html')