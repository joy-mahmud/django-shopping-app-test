from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm
# Create your views here.

def signIn(request):
    if request.method=="POST":
        form = LoginForm(request.POST,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                return HttpResponse(f'welcome {user.username}')
            else:
                return HttpResponse('Invalid credentials')
    
    form=LoginForm()
    return render(request,'users/login.html',{'form':form})
