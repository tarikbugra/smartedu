from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
def user_login(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, 
                                username=username, 
                                password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                
                else:
                    messages.info(request, 'Disabled Account!')
            
            else:
                messages.info(request, 'Wrong username or password!')
        
        else:
            form = LoginForm()

    return render(request, 'login.html', {'form':form})



def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created!')
            return redirect('login')
        else:
            print(form.errors.as_data())
    
    else:
        
        form = RegisterForm()

    return render(request, 'register.html', {'form':form})



def user_logout(request):
    logout(request)
    return redirect('index')


def user_dashboard(request):
    pass





