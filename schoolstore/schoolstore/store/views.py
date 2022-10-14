from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Purchase
from .form import PurchaseForm


# Create your views here.
def home(request):
    return render(request,"home.html")
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/purchase')
        else:
            messages.info(request,"Incorrect Credential")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method =='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password1']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('register')
        return redirect('/')
    return render(request,"registration.html")
def purchase(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        dob=request.POST.get('dob','')
        age=request.POST.get('age','')
        gender=request.POST.get('gender','')
        phno=request.POST.get('phno','')
        mail=request.POST.get('mail','')
        address=request.POST.get('address','')
        department=request.POST.get('department','')
        course=request.POST.get('course', '')
        purpose=request.POST.get('purpose','' )
        material1=request.POST.get('material1','')
        material2=request.POST.get('material2','')
        material3=request.POST.get('material3','')
        material4=request.POST.get('material4','')
        material5=request.POST.get('material5','')
        purchase = Purchase(name=name, dob=dob, age=age, gender=gender, phno=phno, mail=mail, address=address, department=department, course=course, purpose=purpose, material1 = material1, material2 = material2, material3 = material3, material4 = material4, material5 = material5)

        purchase.save()
        return redirect('/final')
    return render(request,'purchase.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def final(request):
    return render(request,"final.html")
