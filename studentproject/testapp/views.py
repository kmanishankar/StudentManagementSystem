from django.shortcuts import render, redirect
from testapp.models import User,Student
from testapp.forms import StudentForm
from django.db.models import Avg, Max, Min, Sum, Count, Q


def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
            user=User.objects.get(username=username,password=password)
        except User.DoesNotExist:
            return render(request,"testapp/login.html",{"error":"Invalid Username or Password"})
        request.session['user_id']=user.id
        request.session['username']=user.username
        request.session['role']=user.role
        if user.role=="admin":
            return redirect("admin_dashboard")
        elif user.role=="student":
            return redirect("student_dashboard")
    return render(request,"testapp/login.html")

def admin_dashboard(request):
    if request.session.get("role")!="admin":
        return redirect("login")
    return render(request,"testapp/admin_dashboard.html")

def student_dashboard(request):
    if request.session.get("role")!="student":
        return redirect("login")
    return render(request,"testapp/student_dashboard.html")
def view_students(request):
    return render(request,"testapp/view_student.html")
def cse_view(request):
    query=request.GET.get("q")
    if query:
        if query.isdigit():
            student=Student.objects.filter(branch="CSE",year=int(query))
        else:
            student=Student.objects.filter(branch="CSE").filter(Q(name__icontains=query) | Q(roll_number__icontains=query))
    else:
        student=Student.objects.filter(branch="CSE")
    return render(request,"testapp/cse.html",{'student':student})
def ece_view(request):
    query=request.GET.get("q")
    if query:
        if query.isdigit():
            student=Student.objects.filter(branch="ECE",year=int(query))
        else:
            student=Student.objects.filter(branch="ECE").filter(Q(name__icontains=query) | Q(roll_number__icontains=query))
    else:
        student=Student.objects.filter(branch="ECE")
    return render(request,"testapp/ece.html",{'student':student})
def eee_view(request):
    query = request.GET.get("q")
    if query:
        if query.isdigit():
            student = Student.objects.filter(branch="EEE", year=int(query))
        else:
            student = Student.objects.filter(branch="EEE").filter(
                Q(name__icontains=query) | Q(roll_number__icontains=query))
    else:
        student = Student.objects.filter(branch="EEE")
    return render(request,"testapp/eee.html",{'student':student})
def civil_view(request):
    query = request.GET.get("q")
    if query:
        if query.isdigit():
            student = Student.objects.filter(branch="CIVIL", year=int(query))
        else:
            student = Student.objects.filter(branch="CIVIL").filter(
                Q(name__icontains=query) | Q(roll_number__icontains=query))
    else:
        student = Student.objects.filter(branch="CIVIL")
    return render(request,"testapp/civil.html",{'student':student})
def mech_view(request):
    query = request.GET.get("q")
    if query:
        if query.isdigit():
            student = Student.objects.filter(branch="MECH", year=int(query))
        else:
            student = Student.objects.filter(branch="MECH").filter(
                Q(name__icontains=query) | Q(roll_number__icontains=query))
    else:
        student = Student.objects.filter(branch="MECH")
    return render(request,"testapp/mech.html",{'student':student})
def delete_view1(request,id):
    details=Student.objects.filter(id=id).delete()
    return redirect("cse")
def delete_view2(request,id):
    details=Student.objects.filter(id=id).delete()
    return redirect("civil")
def delete_view3(request,id):
    details=Student.objects.filter(id=id).delete()
    return redirect("ece")
def delete_view4(request,id):
    details=Student.objects.filter(id=id).delete()
    return redirect("mech")
def delete_view5(request,id):
    details=Student.objects.filter(id=id).delete()
    return redirect("eee")
def edit_view(request,id):
    details=Student.objects.get(id=id)
    form=StudentForm(instance=details)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=details)
        if form.is_valid:
            form.save()
            return redirect("/view_students")
    return render(request,"testapp/edit.html",{'form':form})
def year_wise(request):
    first_year=Student.objects.filter(year=1).count()
    second_year=Student.objects.filter(year=2).count()
    third_year = Student.objects.filter(year=3).count()
    fourth_year = Student.objects.filter(year=4).count()
    return render(request,"testapp/year_wise.html",{'first_year':first_year,
                                            'second_year':second_year,
                                            'third_year':third_year,
                                            'fourth_year':fourth_year})
def first_year_fee_view(request):
    counts=Student.objects.filter(year=1).count()
    paid=Student.objects.filter(year=1,fee_payment="PAID").count()
    notpaid = Student.objects.filter(year=1, fee_payment="NOT PAID").count()
    sum = Student.objects.filter(year=1,fee_payment="NOT PAID").aggregate(Sum('fees'))
    query=request.GET.get("q")
    if query:
        student=Student.objects.filter(year=1).filter(Q(name__icontains=query) | Q(roll_number__icontains=query))
    else:
        student=Student.objects.filter(year=1,fee_payment="NOT PAID").order_by('branch')

    return render(request,"testapp/ffp.html",{'counts':counts,
                                              'paid':paid,
                                              'notpaid':notpaid,
                                              'sum':sum['fees__sum'],
                                              'student':student})
def edit_view1(request,id):
    details=Student.objects.get(id=id)
    form=StudentForm(instance=details)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=details)
        if form.is_valid:
            form.save()
            return redirect("ffp")
    return render(request,"testapp/edit.html",{'form':form})
def second_year_fee_view(request):
    counts=Student.objects.filter(year=2).count()
    paid=Student.objects.filter(year=2,fee_payment="PAID").count()
    notpaid = Student.objects.filter(year=2, fee_payment="NOT PAID").count()
    sum = Student.objects.filter(year=2,fee_payment="NOT PAID").aggregate(Sum('fees'))
    query=request.GET.get("q")
    if query:
        student=Student.objects.filter(year=2).filter(Q(name__icontains=query) | Q(roll_number__icontains=query))
    else:
        student=Student.objects.filter(year=2,fee_payment="NOT PAID").order_by('branch')

    return render(request,"testapp/sfp.html",{'counts':counts,
                                              'paid':paid,
                                              'notpaid':notpaid,
                                              'sum':sum['fees__sum'],
                                              'student':student})
def edit_view2(request,id):
    details=Student.objects.get(id=id)
    form=StudentForm(instance=details)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=details)
        if form.is_valid:
            form.save()
            return redirect("sfp")
    return render(request,"testapp/edit.html",{'form':form})
def third_year_fee_view(request):
    counts=Student.objects.filter(year=3).count()
    paid=Student.objects.filter(year=3,fee_payment="PAID").count()
    notpaid = Student.objects.filter(year=3, fee_payment="NOT PAID").count()
    sum = Student.objects.filter(year=3,fee_payment="NOT PAID").aggregate(Sum('fees'))
    query=request.GET.get("q")
    if query:
        student=Student.objects.filter(year=3).filter(Q(name__icontains=query) | Q(roll_number__icontains=query))
    else:
        student=Student.objects.filter(year=3,fee_payment="NOT PAID").order_by('branch')

    return render(request,"testapp/tfp.html",{'counts':counts,
                                              'paid':paid,
                                              'notpaid':notpaid,
                                              'sum':sum['fees__sum'],
                                              'student':student})
def attendance_view(request):
    first_year=Student.objects.filter(year=1,attendance__lt=75).count()
    second_year=Student.objects.filter(year=2,attendance__lt=75).count()
    third_year = Student.objects.filter(year=3,attendance__lt=75).count()
    fourth_year = Student.objects.filter(year=4,attendance__lt=75).count()

    return render(request,"testapp/attendance.html",{'first_year':first_year,
                                            'second_year':second_year,
                                            'third_year':third_year,
                                            'fourth_year':fourth_year})
def edit_view3(request,id):
    details=Student.objects.get(id=id)
    form=StudentForm(instance=details)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=details)
        if form.is_valid:
            form.save()
            return redirect("tfp")
    return render(request,"testapp/edit.html",{'form':form})
def fourth_year_fee_view(request):
    counts=Student.objects.filter(year=4).count()
    paid=Student.objects.filter(year=4,fee_payment="PAID").count()
    notpaid = Student.objects.filter(year=4, fee_payment="NOT PAID").count()
    sum = Student.objects.filter(year=4,fee_payment="NOT PAID").aggregate(Sum('fees'))
    query=request.GET.get("q")
    if query:
        student=Student.objects.filter(year=4).filter(Q(name__icontains=query) | Q(roll_number__icontains=query))
    else:
        student=Student.objects.filter(year=4,fee_payment="NOT PAID").order_by('branch')

    return render(request,"testapp/fourth.html",{'counts':counts,
                                              'paid':paid,
                                              'notpaid':notpaid,
                                              'sum':sum['fees__sum'],
                                              'student':student})
def edit_view4(request,id):
    details=Student.objects.get(id=id)
    form=StudentForm(instance=details)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=details)
        if form.is_valid:
            form.save()
            return redirect("fourth")
    return render(request,"testapp/edit.html",{'form':form})
def logout_page_view(request):
    return render(request,'testapp/logout.html')
def student_profile(request):
    if request.session.get("role")!="student":
        return redirect("login")
    user_id=request.session.get("user_id")
    try:
        student=Student.objects.get(user_id=user_id)
    except Student.DoesNotExist:
        return render(request,"testapp/profile.html",{'error':"profile no found"})
    return render(request,"testapp/profile.html",{'student':student})
def student_attendance_view(request):
    user_id = request.session.get("user_id")
    student = Student.objects.get(user_id=user_id)
    return render(request, "testapp/student_attendance.html", {"student": student})
def student_fee_view(request):
    user_id = request.session.get("user_id")
    student = Student.objects.get(user_id=user_id)
    return render(request, "testapp/student_fee.html", {"student": student})