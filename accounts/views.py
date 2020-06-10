from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(username=request.POST['username'], email=None, password=request.POST['password'])
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'signup.html', {'error': '비밀번호와 재확인내용이 동일하지 않습니다'})
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'signin.html', {'error':'계정을 다시한번 확인해주세요'})
    return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
    # if request.method == 'POST':
    #     auth.logout(request)
    #     return redirect('index')
    # return render(request, 'signin.html')