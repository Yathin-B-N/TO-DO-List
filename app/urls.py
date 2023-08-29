
from django.contrib import admin
from django.urls import path
from app.forms import TODOform
from app.views import change_todo, delete_todo, home,login, signout,signup, add_todo


urlpatterns = [
    path('',home,name='home'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('add-todo',add_todo,name='add-todo'),
    path('logout',signout),
    path('delete-todo/<int:id>',delete_todo),
    path('change-status/<int:id>/<str:status>',change_todo),



    
]
