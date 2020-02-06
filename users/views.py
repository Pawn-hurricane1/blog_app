from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    # import ipdb;ipdb.set_trace()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'your account have been created....you can now login!!!')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})
@login_required
def profile(request):
    return render(request,'users/profile.html')