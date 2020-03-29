from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Record,Info
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
#from .forms import RecordForm
from accounts.models import Profile
from datetime import date,timedelta
from django.core.mail import send_mail


@login_required(login_url="/accounts/login")
def recordbl(request):
    records = Record.objects.all().order_by('-pub_date')
    
    
    if request.method == 'POST':
        
        if request.POST['name'] and request.POST['description']  and request.POST['email'] and request.POST['amount'] and request.POST['type_of_record'] and request.POST['no_days'] :
            records = Record()
            records.name = request.POST['name']
            records.description = request.POST['description']
            records.amount  = request.POST['amount']
            records.email=request.POST['email']
            records.no_days=request.POST['no_days']
            records.type_of_record=request.POST['type_of_record']
            records.lend_or_borrow_date = date.today()
            records.deadline=records.lend_or_borrow_date + timedelta(days=int(records.no_days))
            records.hunter = request.user
            records.year=int(records.deadline.year)
            records.month=int(records.deadline.month)
            records.day=int(records.deadline.day)
            messages.success(request,f'Your record has been saved !!')
            records.save()
            
            return redirect('recordbl')
        else:
            return render(request, 'records/recordform.html',{'error':'All fields are required.'})
    else:
        paginator = Paginator(records, 3) # Show 5 object per page
        page = request.GET.get('page')
        records = paginator.get_page(page)
        return render(request, 'records/recordform.html',{'records':records})

# Create your views here.
'''@login_required(login_url="/accounts/login")
def recordbl(request):

    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        records=Record()
        

        if form.is_valid():
            records.to_confirm_select_your_username=request.user
            
            form.save()
            records.save()
            

            messages.success(request, f'Your Book has been added !!')
            return redirect('recordbl')
    else:
        form = RecordForm()
    return render(request, 'records/recordform.html', {'form': form})'''

@login_required(login_url="/accounts/login")

def viewrecord(request):
    record=Record.objects.filter(hunter=request.user,type_of_record='lend').order_by('deadline')
    paginator = Paginator(record, 5) # Show 5 object per page
    page = request.GET.get('page')
    record = paginator.get_page(page)
    date1=date.today()
    year=int(date1.year)
    month=int(date1.month)
    day=int(date1.day)
    return render(request, 'records/viewlendrecords.html',{'record':record,'years':year,'months':month,'days':day})

def viewborrowrecord(request):
    record=Record.objects.filter(hunter=request.user,type_of_record='borrow').order_by('deadline')
    paginator = Paginator(record, 5) # Show 5 object per page
    page = request.GET.get('page')
    record = paginator.get_page(page)
    return render(request, 'records/viewborrowrecords.html',{'record':record})

def deleteb(request, records_id):
    if request.method == 'POST':
        deleteinstance = get_object_or_404(Record, pk=records_id)
        if deleteinstance.type_of_record=='lend':
            messages.success(request,f'Your record has been Deleted !!')
            deleteinstance.delete()
            return redirect('dell')
        else:
            messages.success(request,f'Your record has been Deleted !!')
            deleteinstance.delete()
            return redirect('delb')

    

def delb(request):
    record=Record.objects.filter(hunter=request.user,type_of_record='borrow').order_by('deadline')
     
    paginator = Paginator(record, 5) # Show 5 object per page
    page = request.GET.get('page')
    record = paginator.get_page(page)
    return render(request, 'records/deleteviewb.html',{'record':record})

def dell(request):
    record=Record.objects.filter(hunter=request.user,type_of_record='lend').order_by('deadline')
    paginator = Paginator(record, 5) # Show 5 object per page
    page = request.GET.get('page')
    record = paginator.get_page(page)
    return render(request, 'records/deleteviewl.html',{'record':record})

@login_required(login_url="/accounts/login")

def create(request):
    infos = Info.objects.filter(hunter=request.user).order_by('-spent_date')
    if request.method == 'POST':
        
        if request.POST['description'] and request.POST['amount']  :

            
            if type(request.POST['amount']) is float or int:
                if int(request.POST['amount']) > 0:
                    infos = Info()
                    infos.description = request.POST['description']
                    infos.amount  = request.POST['amount']
                    infos.spent_date=timezone.datetime.now()
                    infos.hunter = request.user
                    messages.success(request,f'Your record has been saved !!')
                    infos.save()
                    return redirect('create')
                else:
                    messages.error(request,f'plzz enter Positive value !!')
                    return render(request, 'records/grecords.html')
               
            else:
                messages.error(request,f'plzz enter valid value !!')
                return render(request, 'records/grecords.html')
                

            
            
            
            
        else:
            return render(request, 'records/grecords.html',{'error':'All fields are required.'})
    else:
        paginator = Paginator(infos, 5) # Show 5 object per page
        page = request.GET.get('page')
        infos = paginator.get_page(page)
        return render(request, 'records/grecords.html',{'infos':infos})



    

    
    

   
    