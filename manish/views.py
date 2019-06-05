from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')

def count(request):
    data=request.GET['fulltextarea']
    li=data.split()
    no=len(li)
    worddic={}
    for word in li:
        if word in worddic:
            worddic[word]+=1
        else:
            worddic[word]=1

    return render(request,'count.html',{'Text':data,'Number':no,'worddic':worddic.items()})
def about(request):
    return render(request,'about.html')
