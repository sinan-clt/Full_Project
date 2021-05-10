from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test1(request):
    return HttpResponse ('<h1 align="center">hellloooo</h1>')
def test2(request):
    return render(request,'head.html')