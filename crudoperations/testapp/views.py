from django.shortcuts import render,redirect
from testapp.forms import DetailsForm
from django.contrib.auth.decorators import login_required
from testapp.models import Details
def home_view(request):
    return render(request,'testapp/base.html')
@login_required
def add_view(request):
    form=DetailsForm()
    if request.method=='POST':
        form=DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/add.html',{'form':form})
@login_required()
def view_view(request):
    list=Details.objects.all()
    return render(request,'testapp/display.html',{'list':list})
# Create your views here.
def delete_view(request,id):
    details=Details.objects.get(id=id)
    details.delete()
    return redirect('/view')
def edit_view(request,id):
    details=Details.objects.get(id=id)
    form=DetailsForm(instance=details)
    if request.method=='POST':
        form=DetailsForm(request.POST,instance=details)
        if form.is_valid():
            form.save()
            return redirect('/view')
    return render(request,'testapp/edit.html',{'form':form})
def logout_page_view(request):
    return render(request,'testapp/logout.html')