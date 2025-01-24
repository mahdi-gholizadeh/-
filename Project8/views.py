


from django.shortcuts import render,redirect
from django.shortcuts import Http404,HttpResponse
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.models import User
from .forms import ContactForm,Loginform,Registerform
def home(request):
    context={
        'message':"welcome to my site"

    }
    return render(request,'home.html',context)


def about_us(request):
    context={
        'about_message':"made by mahdi"

    }

    return render (request,'about_us.html',context)


def contact_us(request):
    contact_form=ContactForm()
    if request.method=='POST':
        print(request.POST.get('Fullname'))
        print(request.POST.get("Email"))
        print(request.POST.get("message"))
    context={
       'contact_form':contact_form

    }
    return render(request,'contact_us.html',context)


def loginpage(request):
    print(request.user.is_authenticated)
    form=Loginform(request.POST or None)
    if form.is_valid():
        userName=form.cleaned_data.get('username')
        print(userName)
        password=form.cleaned_data.get('password')
        print(password)
        user=authenticate(request,username=userName,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            print("چنین کاربری وجود ندارد")
    context = {
        "message":"صفحه ورود",
        "loginform":form

    }

    return render(request, 'auth/login.html', context)





User=get_user_model()


def register_page(request):
    register_form = Registerform(request.POST or None)

    if register_form.is_valid():

        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('Email')
        password = register_form.cleaned_data.get('password')


        User.objects.create_user(username=username, email=email, password=password)

    context = {
        "message": "فرم ثبت نام",
        "register_form": register_form
    }

    return render(request, 'register.html', context)




def log_out(request):
    logout(request)
    return redirect('/')