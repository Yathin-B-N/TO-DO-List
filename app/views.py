from django.forms import Form
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login as loginuser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from app.forms import TODOform
from app.models import TODO
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
   if request.user.is_authenticated:
      user = request.user

      form = TODOform()
      todos = TODO.objects.filter(user = user).order_by('priority')
      print(todos)
      return render(request,'index.html',context = { 'form' : form , 'todos':todos})


def login(request):
   if request.method == "GET":
       form1 = AuthenticationForm()
       context ={
      "form" : form1
       }
       return render(request,'login.html',context = context)

   else:
      form1 = AuthenticationForm(data = request.POST)
      print(form1.is_valid)
      print(request.POST)
      if form1.is_valid():
         username= form1.cleaned_data.get('username')
         password = form1.cleaned_data.get('password')
         user = authenticate(username=username,password=password)
         if user is not None:
            loginuser(request , user)
            return redirect('home')
      else:
         context = {
            "form" : form1
         }
         return render(request,'login.html',context = context)
           
def signup(request):
 if request.method == 'GET':
   form = UserCreationForm()
   context = {
      "form" : form
   }
   return render(request,'signup.html',context=context)
 else:
   form = UserCreationForm(request.POST)
   context = {
      "form" : form
   }
 
   if form.is_valid():
     user = form.save()
     print(user)
     if user is not None:
          return redirect('login')

   
   else:
       return render(request,'signup.html',context=context)
   
@login_required(login_url='login')
def add_todo(request):
   if request.user.is_authenticated:
      user = request.user
      print(user)
      form = TODOform(request.POST)
      if form.is_valid():
         print(form.cleaned_data)
         todo = form.save(commit=False)
         todo.user = user
         todo.save()
         return redirect("home")
      else:
         return render(request,'index.html',context = { 'form' : form})


def signout(request):
   logout(request)
   return redirect('login')

def delete_todo(request , id):
   TODO.objects.get(pk = id).delete()
   return redirect('home')


def change_todo(request , id, status):
   todo = TODO.objects.get(pk = id)
   todo.status= status
   todo.save()
   return redirect('home')


     
