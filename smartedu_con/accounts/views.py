from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from courses.models import Course
from django.contrib.auth.models import User



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



@login_required(login_url='login')
def user_dashboard(request):
    current_user = request.user
    courses = current_user.course_person.all()

    context = {
        'courses': courses
    }

    return render(request, 'dashboard.html', context)



def enroll(request):
    course = Course.objects.get(id=request.POST['course_id'])
    user = User.objects.get(id=request.POST['user_id'])
    course.person.add(user)
    return redirect('dashboard')


def release(request):
    course = Course.objects.get(id=request.POST['course_id'])
    user = User.objects.get(id=request.POST['user_id'])
    course.person.remove(user)
    return redirect('dashboard')






