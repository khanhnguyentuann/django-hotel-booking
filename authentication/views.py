from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Đăng ký thành công! Bạn có thể đăng nhập.')
            return redirect('authentication:login')
    else:
        form = RegisterForm()
    
    if form.errors:
        for field in form:
            for error in field.errors:
                messages.error(request, f"{field.label}: {error}")

    return render(request, 'authentication/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('homepage:index')
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không chính xác.')
    return render(request, 'authentication/login.html')


def account(request):
    # code xử lý cho trang quản lý tài khoản
    return render(request, 'authentication/account.html')


def logout_view(request):
    logout(request)
    return redirect('authentication:login')