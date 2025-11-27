from django.contrib import admin
from testapp.models import User,Student
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','password','role']
admin.site.register(User,UserAdmin)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','user','roll_number','name','gender','father_name','branch','year',
                    'attendance','fees','fee_payment']
admin.site.register(Student,StudentAdmin)
# Register your models here.
