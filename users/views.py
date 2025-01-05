from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm,RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
# Create your views here.

def signIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        form = LoginForm(request.POST,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request,user)
                return redirect('home')
    
    form=LoginForm()
    return render(request,'users/login.html',{'form':form})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})

       
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
