from django.shortcuts import render
from django.http import HttpResponse
from home.forms import StudentForm,infoForm
from home.models import student
from django.db import connection
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
        form = StudentForm(request.POST)
        newStudent = form.save()
        return HttpResponse("<h1>success</h1>")
    else:
        form = StudentForm()
        return render(request,"input.html",{'form':form})
    
# def getinfo(request):
#     # if request.method == "POST":
#     #     form = infoForm(request.POST)
#     #     print(form)
#     #     name = form.cleaned_data['name']
#     #     one_student = student.objects.get(Name=name)
#     #     return render(request,"infoViewer.html",{'student':one_student})
#     #     #do something
#     # else:
#     #     newForm =infoForm()
#     #     return render(request,"studentInfo.html",{'form':newForm})

#     all_students = student.objects.all()
#     return render(request,"infoViewer.html",{"student":all_students})

def getinfo(request):
    # pupil = student.objects.get(pk=2)
    # pupil_Cls = 2
    # pupil.save()
    # all_students = student.objects.all()
    # # for s in all_students:
    # #     s.Cls = 11
    # #     s.save()


    # return render(request,"infoViewer.html",{'student':all_students})
    cursor = connection.cursor()
    sql = "SELECT * FROM student"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    all_students = []
    for row in result:
        name=row[1]
        clas=row[2]
        roll=row[3]
        one={'Name':name,'Cls':clas,'Roll':roll}
        all_students.append(one)
        
        return render(request,"infoViewer.html",{'student':all_students})