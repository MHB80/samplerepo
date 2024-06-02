from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import reports,auth_user
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
# Create your views here.
def user_login(request):

    if request.method == "GET":
        return render(request, 'login.html')
        # return render(request,'formstemplate.html')
        
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        # print("****")
        # print(username)
        user = authenticate(username=username, password=password)
        if user is not None:
            print("authenticated")
            return render(request,'formstemplate.html')
        else:
            context = {"error":"invalid user or password"}
            print('bye')
            return render(request,"login.html",context)
        return render(request,'login.html')
    # Invalid credentials
    # Handle accordingly (e.g., show an error message)
def form_data_view(request):
    print(request.method)
    if request.method == "POST":        
        print('this is post')
        Q1 =request.POST.get('q1')
        Q2 =request.POST.get('q2')
        Q3 =request.POST.get('q3')
        report = reports(Quality=Q1, Date=Q2, city=Q3)
        report.save()
    # else:   
        return render(request,'formstemplate.html')   
def User_logout_view(request):
    # print("hello")
    logout(request)
    return redirect('login')

