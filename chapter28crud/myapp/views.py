from django.shortcuts import render,redirect

from .forms import employeeform
from .models import employee
def home(request):
    return render(request,'home.html')
def create(request):
    if request .method=='POST':
        myform=employeeform(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('read')
        return redirect('create')
    else:
        myform=employeeform
        return render(request,'create.html',{'form':myform})
# def update(request):
#     return render(request,'update.html')
# def delete(request):
#     return render(request,'delete.html')






# Create your views here.
