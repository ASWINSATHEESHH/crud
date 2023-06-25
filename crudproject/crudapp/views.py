from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Project

# Create your views here.
def Home(request):
    return render(request, 'home.html')
def Contact(request):
    return render(request,'contact.html')
def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')
def Login(request):
    error= ""
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d={'error':error}
    return render(request,'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    
    logout(request)
    return redirect('login')

def View_Project(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Project.objects.all()
    d = {'doc': doc}
    return render(request, 'Viewproject.html', d)


def Delete_Project(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    developer= Project.objects.get(id=pid)
    developer.delete()
    return redirect('viewproject')

def Add_Project(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        n=request.POST['name']
        m=request.POST['mobile']
        p=request.POST['project']
        try:
            Project.objects.create(Name=n, mobile=m, project=p)
            error ='no'
        except:
            error= 'yes'
    d = {'error': error }
    return render(request,'addproject.html',d)

