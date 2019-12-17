from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth

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
                print("cant take this username")
                return redirect("/")   
            elif User.objects.filter(email=email).exists():
                print("cant take this email id already taken")
                return redirect("/")   
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=firstName,last_name=lastName)
                user.save()
                print("user created")
        else:
            print("password dont match")
            return redirect("/")


    else:
        return render(request,'register.html')

