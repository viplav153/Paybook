from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm ,UserUpdateForm,ProfileUpadteForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.utils import timezone
from records.models import Info,Record
from datetime import date,timedelta


# Create your views here.
def signup(request):
    if request.method =='POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html',{'form':form})
    
    


@login_required
def profile(request):
    if request.method =='POST' :
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpadteForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid()and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account Account updated !!')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpadteForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form,
    
    }

    return render(request,'accounts/profileupdate.html',context)




    #if request.method =='POST' :
    #    a=Profile.objects.get(id=2
    #    a-=1
    #    a.save()
    #    return render(request,'accounts/profile.html')

@login_required    
def change_password(request):
    if request.method =='POST' :
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,f'Your account Password has been updated !!')
            return redirect('profile_view')
        else:
            messages.error(request,f'something went wrong!!')
            return redirect('change_password')


    else:
        form =PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'accounts/password.html',args)



@login_required
def profile_view(request):
    record=Info.objects.filter(hunter=request.user,).order_by('spent_date')
    record1=Record.objects.filter(hunter=request.user,type_of_record='borrow')
    record2=Record.objects.filter(hunter=request.user,type_of_record='lend')
    time_now=timezone.now()
    total30=0
    last_30days=time_now-timedelta(days=int(30))
    for each in record:
        if each.spent_date >= last_30days:
            total30=int(each.amount)+int(total30)
    
    no_lenders=0
    no_borrower=0
    for each in record1:
        no_lenders=no_lenders+1

    for each in record2:
        no_borrower=no_borrower+1
    
    p_form=ProfileUpadteForm(instance=request.user.profile)
    return render(request,'accounts/profile.html',{'p_form':p_form,'total30':total30,'no_borrower':no_borrower,'no_lenders':no_lenders})


   
        

        


    
    
    

