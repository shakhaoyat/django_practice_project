from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    dict_user=[]
    x={"Name":"Shakhaoyat","Email":shakhaoyat@xyz.com}
    dict_user.append(x)
    x={"Name":"Hossain","Email":Hossain@xyz.com}
    dict_user.append(x)
    x={"Name":"Chad","Email":Chad@xyz.com}
    dict_user.append(x)
    return render(request,"demo.html",{"Users":dict_user})
def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")
