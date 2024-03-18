from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name='home'),
    path("fileupload/", views.FileUpload, name='upload'),
    
]
