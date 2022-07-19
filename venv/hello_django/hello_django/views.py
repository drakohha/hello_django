from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    #return HttpResponse('что то идет не так')
    a =5+6
    return render(request,'about.html',{'Grotting': a})

def home(request):
    return HttpResponse('this is my home')
