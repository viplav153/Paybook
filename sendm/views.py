from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
#from .forms import RecordForm
from accounts.models import Profile
from datetime import date,timedelta
from django.core.mail import send_mail
from records.models import Record



def index(request,pk):
    if request.method == 'POST':
        s = get_object_or_404(Record, pk=pk)
        reciever=str(s.email)
        subject='regarding borrowed money from '+str(s.hunter)
        text='hey you had borrowed RS '+str(s.amount)+' the deadline is over plzz return the amount '
        send_mail(subject,text,'contact@viplavanand.co',
                [reciever],fail_silently=False)
        return render(request,'sendm/index.html')

