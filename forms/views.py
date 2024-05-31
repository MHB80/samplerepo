from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import reports,auth_user
from django.contrib.auth import authenticate,login
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = auth_user()
        print('hello')
        if username == None or password==None:
            print(username,password)
            context = {"error":"invalid user or password"}
            print('bye')
            return render(request,"login.html",context)
        elif user.isvalid(username,password):
            print('this is nice')
            return render(request,'/formstemplate.html')
        else:
            print('not true')
            context = {"error":"invalid user or password"}

    return render(request,'login.html')

# def formpage(request):

#     return render(request,'formstemplate.html')
    
def forms(request):
    if request.method == 'POST':
        # getting the items from the html
        Quality = request.POST.get('')
        Date = request.POST.get('')
        city = request.POST.get('')
        # create the items of reports class
        entry = reports(Quality=Quality,Date=Date,city=city)
        # add them to the database
        entry.save()

        return HttpResponse("completed the insertion")
    else:
        return HttpResponse("invalid")

