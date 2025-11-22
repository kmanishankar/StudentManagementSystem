from django.contrib import admin
from testapp.models import Details
class DetailsAdmin(admin.ModelAdmin):
    list_display = ['id','roomno','name','fees','address']
admin.site.register(Details,DetailsAdmin)
# Register your models here.
