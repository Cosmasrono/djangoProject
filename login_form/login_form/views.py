from django.shortcuts import render  
from login_form.form import studentForm  

def index(request):
    student=studentForm()
    return render(request,'index.html',{'form':student})