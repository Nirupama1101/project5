from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def India(request):
    return HttpResponse("Won the match") 

def test1(request):
    return render(request,'test1.html')