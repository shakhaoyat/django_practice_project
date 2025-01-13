from django.shortcuts import render
from django.http import HttpResponse
from home.forms import studentForm
# Create your views here.


def home(request):
    dict_user=[]
    x={"Name":"Shakhaoyat","Email":"shakhaoyat@xyz.com"}
    dict_user.append(x)
    x={"Name":"Hossain","Email":"Hossain@xyz.com"}
    dict_user.append(x)
    x={"Name":"Chad","Email":"Chad@xyz.com"}
    dict_user.append(x)

    dict=[]
    x={"Name":"Asif","Prof":"Teacher"}
    dict.append(x)
    x={"Name":"Shams","Prof":"Student"}
    dict.append(x)
    return render(request,"demo.html",{"Users":dict_user,"User2":dict})
def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")
def studentForm(request):
    if request.method == "POST":
        form = studentForm()
    return render(request,"input.html",{'form':form})