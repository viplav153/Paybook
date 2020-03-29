from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime,date
from django.utils import timezone
from django.contrib.auth.models import User




class Record(models.Model):
    name= models.CharField(max_length=255)
    lend_or_borrow_date = models.DateField()
    deadline= models.DateField()
    no_days=models.IntegerField(default = 1)
    description = models.TextField()
    amount=models.IntegerField(default = 0)
    hunter= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length = 100, blank=True)
    type_of_record=models.CharField(max_length = 100, blank=True)
    year=models.IntegerField(default = 1)
    month=models.IntegerField(default = 1)
    day=models.IntegerField(default = 1)

    def __str__(self):
        return self.name
    
    def summary(self):
        return self.description[:100]

    def pub_date_pretty(self):
        return self.lend_or_borrow_date.strftime('%b %e %y')
    
    def pub_date_deadline(self):
        return self.deadline.strftime('%b %e %y')

    

    


class Info(models.Model):
    description = models.TextField()
    amount=models.IntegerField(default = 0)
    hunter= models.ForeignKey(User,on_delete=models.CASCADE)
    spent_date= models.DateTimeField()

    
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)


