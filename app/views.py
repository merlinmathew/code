from django.contrib.auth import authenticate,login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import Loginform,Registerform
from django.contrib.auth.decorators import login_required
from .models import Blog,UserProfile
from django.contrib.auth.models import User
# Create your views here.

@login_required
def home(request):

    try:
        userprofile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        userprofile = UserProfile.objects.create(user=request.user)
    posts=Blog.objects.filter(user=userprofile).order_by('published_date')
    return render(request,"app/blog_list.html",{'posts':posts,'user':userprofile.user})

def login2(request):
    f = Loginform(request.POST)
    if request.method=='POST':
        if f.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = authenticate(username=username, password=password)
                #user = UserProfile.objects.get(username=username, password=password)#for custom


                if user is not None:
                    login(request,user)
                    #posts=Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
                    #return render(request,"app/blog_list.html",{'posts':posts,'user':user})
                    userprofile = UserProfile.objects.get(user=request.user)
                    posts=Blog.objects.filter(user=userprofile).order_by('published_date')
                    return render(request,"app/blog_list.html",{'posts':posts,'user':userprofile.user})
                    #h = Blog.objects.all().order_by('-blog_time')

                    #return HttpResponseRedirect("/add_post/")

                else:
                    return render(request, "app/login.html", { 'form': f, 'msg': 'user does not exist' })

            except ObjectDoesNotExist:
                return render(request, "app/login.html", { 'form': f, 'msg': '' })
        else:
            return render(request, "app/login.html", {'form':f ,'msg': 'validation error' })

    f = Loginform()
   # post=PostForm()
    return render(request, 'app/login.html',{'form':f})

def register(request):
    if request.method == 'POST':
        user_form = Registerform(request.POST)
        if user_form.is_valid():
            #up=UserProfile() #for custom
            #up.username = user_form.cleaned_data.get('username')#for custom
            username = user_form.cleaned_data.get('username')
            #user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')
            #user.set_password(password)
            email = user_form.cleaned_data.get('email')
            #user.set_password(password)
            #dob = user_form.cleaned_data.get('dob')
            g = User.objects.create_user(username=username,password=password,email=email)
            #user.set_password(password)
            #up.save()#for custom
            g.save()

            #new_user = authenticate(username=username, password=password)
            #login(request, new_user)

            #posts=Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            #return render(request,"app/blog_list.html",{'posts':posts})
            lform=Loginform(request.POST)
            return HttpResponseRedirect('/login/')

        else:
            user_form = Registerform()
            return render(request,
                          'app/login.html',
                          {'user_form': user_form, 'error_message': "Please Enter Valid Data"})

    else:
        user_form = Registerform()
       # posts=PostForm()
    return render(request,'app/register.html',{'user_form': user_form})

def post_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    return render(request, 'app/post_detail.html', {'post': post})


def prof_edit(request,pk):
    g = get_object_or_404(User, pk=pk)
    #g = UserProfile.objects.get(pk=request.user.id)
    f=Registerform(request.POST)
    context={}
    if request.POST:
        if f.is_valid():

            username1 = request.POST.get("username")

            password2 = request.POST.get("password")
            email3 = request.POST.get("email")
            print(username1,password2,email3)
            #dob4= request.POST.get("dob")
            g.username=username1
            g.set_password=password2
            g.email=email3
            #g.dob=dob4
            g.save()
            context['msg'] = 'edited  successfully'
            f=Registerform()
            return render(request, "app/prof_edit.html", {'form':f, 'msg': 'Updated successfully' })
        else:
            return render(request, "app/prof_edit.html", {'form': f, 'msg': 'some errors'})

    data = {'username': g.username, 'email': g.email}#, 'dob': g.dob }
    f = Registerform(initial=data)
    return render(request, "app/prof_edit.html", {'form': f, 'msg': ''})


def logout2(request):

    logout(request)
    return HttpResponseRedirect("/login/")




