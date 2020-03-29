from django.urls import path,include

from . import views


urlpatterns = [
   
    path('recordbl',views.recordbl,name='recordbl'),
    path('viewrecord',views.viewrecord,name='viewrecord'),
    path('viewborrowrecord',views.viewborrowrecord,name='viewborrowrecord'),
    path('<int:records_id>/', views.deleteb, name='deleteb'),
    path('delb',views.delb,name='delb'),
    
    path('dell',views.dell,name='dell'),
    path('create',views.create,name='create'),
    
   
    
    
    
    
]