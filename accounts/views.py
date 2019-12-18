from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method=='POST':
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        email=request.POST['email']
        username=request.POST['userName']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        if password== confirmPassword: 

            if User.objects.filter(username=username).exists():
                messages.info(request,"UserName taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register') 
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=firstName,last_name=lastName)
                user.save()
                print("user created")
                return redirect("login")
        else:
            messages.info(request,"password dont match")
            return redirect('register')


    else:
        return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid details")
            return redirect("login")
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")
