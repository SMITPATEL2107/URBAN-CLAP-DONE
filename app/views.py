from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *
from random import randint
from.utils import *

# Create your views here.
def index(request):
    return render(request,"app/ind.html")

def indexpage(request):
    return render(request,"app/index1.html")

def Login(request):
    return render(request,"app/login.html")

def About(request):
    return render(request,"app/about.html")

def Serviceman(request):
    return render(request,"app/service_man.html")

def Service(request):
    return render(request,"app/service.html")

def BookPage(request):
    return render(request,"app/address.html")

def RegisterUser(request):
    try:
        if request.POST['role'] == 'technician':
            print("--------------1---------------")
            role = request.POST['role']
            fullname=request.POST['fname']
            email=request.POST['email']
            phone=request.POST['phone']
            password=request.POST['password']
            reapeatpassword=request.POST['reapeatpassword']
            user = User.objects.filter(email=email)
            if user:
                print("--------------2---------------")
                message = 'This email already exists'
                return render(request, 'app/index.html', {'message': message})
            else:
                if password == reapeatpassword:
                    print("--------------3---------------")
                    otp = randint(100000, 9999999)
                    newuser = User.objects.create(
                        email=email, password=password, role=role, otp=otp)
                    newtech = technician.objects.create(user_id=newuser, fullname=fullname,phone=phone)
                    return render(request, 'app/login.html')
                else:
                    message = "Password and confirm password doesn't match"
                    return render(request, 'app/index.html', {'message': message})
        else:
            print("--------------4---------------")
            role = request.POST['role']
            fullname=request.POST['fname']
            email=request.POST['email']
            phone=request.POST['phone']
            password=request.POST['password']
            reapeatpassword=request.POST['reapeatpassword']
            
            user = User.objects.filter(email=email)
            if user:

                message = 'This email already exists'
                return render(request, 'app/index.html', {'message': message})
            else:
                if password == reapeatpassword:
                    print("--------------5---------------")
                    otp = randint(100000, 9999999)
                    newuser = User.objects.create(
                        email=email, password=password, role=role, otp=otp)
                    newcus = customer.objects.create(user_id=newuser, fullname=fullname,phone=phone)
                    return render(request, 'app/login.html')
                else:
                    message = "Password and confirm password doesn't match"
                    return render(request, 'app/index.html', {'message': message})

    except Exception as e1:
        print("Registration print---->",e1)

def LoginUser(request):
    if request.POST['role'] == 'technician':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        print(user)
        if user[0]:
            if user[0].password == password and user[0].role == 'technician':
                techni= technician.objects.filter(user_id=user[0])
                #return render(request,"app/tech.html")
                return redirect('alldata')
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "app/login.html", {'message': message})
        else:
            message = "user doesn't exist"
            return render(request, "app/login.html", {'message': message})

    if request.POST['role'] == 'customer':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        print(user)
        if user:
            if user[0].password == password and user[0].role == 'customer':
                custo = customer.objects.filter(user_id=user[0])
                
                return render(request,"app/loginservice.html")
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "app/login.html", {'message': message})
        else:
            message = "user doesn't exist"
            return render(request, "app/login.html", {'message': message})

def BookNow(request):
    return render(request, 'app/index1.html')
    if request.POST['role'] == 'technician':
            print("--------------1---------------")
            role = request.POST['role']
            fullname=request.POST['fname']
            email=request.POST['email']
            phone=request.POST['phone']
            password=request.POST['password']
            reapeatpassword=request.POST['reapeatpassword']
            user = User.objects.filter(email=email)
            if user:
                print("--------------2---------------")
                message = 'This email already exists'
                return render(request, 'app/index.html', {'message': message})
            else:
                if password == reapeatpassword:
                    print("--------------3---------------")
                    otp = randint(100000, 9999999)
                    newuser = User.objects.create(
                        email=email, password=password, role=role, otp=otp)
                    newtech = technician.objects.create(user_id=newuser, fullname=fullname,phone=phone)
                    return render(request, 'app/login.html')
                else:
                    message = "Password and confirm password doesn't match"
                    return render(request, 'app/index.html', {'message': message})
    else:
        print("--------------4---------------")
        role = request.POST['role']
        fullname=request.POST['fname']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        reapeatpassword=request.POST['reapeatpassword']
        
        user = User.objects.filter(email=email)
        if user:

            message = 'This email already exists'
            return render(request, 'app/index.html', {'message': message})
        else:
            if password == reapeatpassword:
                print("--------------5---------------")
                otp = randint(100000, 9999999)
                newuser = User.objects.create(
                    email=email, password=password, role=role, otp=otp)
                newcus = customer.objects.create(user_id=newuser, fullname=fullname,phone=phone)
                             
                return render(request, 'app/newpage.html')
            else:
                message = "Password and confirm password doesn't match"
                return render(request, 'app/index.html', {'message': message})
                if request.POST['role'] == 'technician':
                    email = request.POST['email']
                    password = request.POST['password']
                    user = User.objects.filter(email=email)
                    print(user)
                    if user[0]:
                        if user[0].password == password and user[0].role == 'technician':
                            techni= technician.objects.filter(user_id=user[0])
                            
                            
                            return render(request,"app/tech.html")
                        else:
                            message = "Your password is incorrect or user doesn't exist"
                            return render(request, "app/login.html", {'message': message})
                    else:
                        message = "user doesn't exist"
                        return render(request, "app/login.html", {'message': message})

                if request.POST['role'] == 'customer':
                    email = request.POST['email']
                    password = request.POST['password']
                    user = User.objects.filter(email=email)
                    print(user)
                    if user:
                        if user[0].password == password and user[0].role == 'customer':
                            custo = customer.objects.filter(user_id=user[0])
                            
                            
                            return render(request,"app/cust.html")
                        else:
                            message = "Your password is incorrect or user doesn't exist"
                            return render(request, "app/login.html", {'message': message})
                    else:
                        message = "user doesn't exist"
                        return render(request, "app/login.html", {'message': message})


    
def Insert(request):
    address=request.POST['add']
    role=request.POST['role']
    phone=request.POST['phone']
    email=request.POST['email']

    newmain=Main.objects.create(address=address,phone=phone,email=email,role=role)
    user=Main.objects.filter(email=email)
    if user:
        email_subject="Account Verification Mail"
        sendmail(email_subject,"mail_template",email,{'email':email,'phone':phone})
        return render(request,("app/thanks.html"))
    else:
        return render(request,("app/sorry.html"))   

def AllData(request):
    alldata = Main.objects.all()
    cont={'alldata':alldata}
    return render(request,"app/tech.html",cont)

def Accept(request,pk):
    #address=request.POST['address']
    getdata =Main.objects.get(pk=pk)
    return render(request,"app/emailconform.html",{'key2':getdata})

def Conform(request):
    email=request.POST['email']
    
    new=Main.objects.create(email=email)
    user=Main.objects.filter(email=email)
    if user:
        email_subject="Request Conformation"
        sendmail(email_subject,"mail_template1",email,{'email':email})
        return render(request,("app/sucess.html"))
    else:
        return render(request,("app/sorry.html")) 