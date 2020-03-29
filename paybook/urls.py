from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views 
from records import views as r_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('records/',include('records.urls')),
    path('sendm/',include('sendm.urls')),
   path('',r_view.create,name='create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
