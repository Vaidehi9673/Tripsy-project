from django.shortcuts import render , redirect
from django.http import HttpResponse
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
# Create your views here.
def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    if request.method=="POST":
        uname=request.POST['uname']
        email=request.POST['email']
        text=request.POST['text']
        #print(uname, email, text)
        con = Contact(uname=uname, email=email, text=text)
        con.save()
        messages.success(request, 'Message has been sent succesfully!')
        return redirect("/")
    else:
        messages.error(request, 'Please try again')
        return render(request, "home/contact.html")

def blog(request):
    return render(request, "home/blog.html")
def blogpost(request):
    return HttpResponse("blogpost page")

def conditions(request):
    return HttpResponse("conditions page")

def signup(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        pwd1=request.POST['pwd1']
        #print(fname, lname,email,uname,pwd,pwd1)
        #checking validations
        if(len(fname)>3 and len(lname)>2 and len(uname)>4 and pwd == pwd1):
            user = User.objects.create_user(uname , email, pwd)
            user.fname = fname
            user.lname = lname
            user.save()
            messages.success(request, 'Registered successfully')
            return redirect("/")
        else:
            messages.error(request, 'Please try again')
            return redirect("/")

def transfersign(request):
    return render(request, "home/signup.html")

def handlelogin(request):
    if request.method=="POST":
       loginuser=request.POST['loginuser']
       loginpass=request.POST['loginpass']
       user = authenticate(username=loginuser, password=loginpass)
       if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect("/")
       else:
            messages.error(request, 'Please try to login again')
            return redirect("/")

def transferlogin(request):
    return render(request, "home/login.html")

def handlelogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect("/")