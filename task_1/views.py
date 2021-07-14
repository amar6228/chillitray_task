from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from task_1.models import Task
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    task=Task.objects.all()
    print(task)
    context={'task':task}
    return render(request, 'task_1/task_1.html', context)


# authenticate APIs
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        print(username,fname,phone,email,pass1,pass2)

        if len(username)>10:
            messages.error(request,"username not greater than 10")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"username should contain letter and number only")
            return redirect('home')

        if pass1!=pass2:
            messages.error(request,"Password not matched")
            return redirect('home')     
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, "your account created successfully")
        return redirect('home')
    else:
        return HttpResponse ('404 - Not found')
    
def login(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'successfully logged in')
            return redirect('home')
        else:
            messages.error(request, "invalid credentials, try again")
            return redirect('home')
    else:
        return HttpResponse('404 - Not found')

def logout(request):
    # if request.method=='POST':
    logout(request)
    messages.success(request, "Successfully logout")
    return redirect('home')



























