from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def view1(request):
    return HttpResponse("<h1>hill hello </h1>")

def view2(request):
    return render(request,"sam1.html")

def view3(request,data):
    return HttpResponse(f"enter data is ;{data}")

def view4(request,name):
    return render(request,"sam2.html",context={'name':name})


def view5(request):
    login=True
    return render(request,"sam3.html",context={"login":login})

def view6(request):
    login=True
    return render(request,"sam4.html",context={"login":login,"login1": ["home","message","notification"],"logout":['sigup', 'frogetpassword']})


def view7(request):
    login=False
    return render(request,"sam5.html",context={"login":login,'profile':{'name':"sharansiddesh",'age':24,'phone':'8971903742','email':'sharansiddesh99@gmail.com'}})


