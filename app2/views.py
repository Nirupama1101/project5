from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def Aus(request):
    return HttpResponse("Lost the match") 

def test2(request):
    return render(request,'test2.html')