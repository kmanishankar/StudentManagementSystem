"""
URL configuration for studentproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view,name="login"),
    path('admin_dashboard/',views.admin_dashboard,name="admin_dashboard"),
    path('student_dashboard/',views.student_dashboard,name="student_dashboard"),
    path('view_students/',views.view_students,name="view_students"),
    path('cse_view/',views.cse_view,name="cse"),
path('ece_view/',views.ece_view,name="ece"),
path('eee_view/',views.eee_view,name="eee"),
path('civil_view/',views.civil_view,name="civil"),
path('mech_view/',views.mech_view,name="mech"),
    path('edit/<int:id>',views.edit_view),
path('edit1/<int:id>',views.edit_view1),
path('edit2/<int:id>',views.edit_view2),
path('edit3/<int:id>',views.edit_view3),
path('edit4/<int:id>',views.edit_view4),
    path('delete1/<int:id>',views.delete_view1),
path('delete2/<int:id>',views.delete_view2),
path('delete3/<int:id>',views.delete_view3),
path('delete4/<int:id>',views.delete_view4),
path('delete5/<int:id>',views.delete_view5),
    path('year_wise/',views.year_wise),
path('at_details/',views.attendance_view),
    path('ffp_details/',views.first_year_fee_view,name="ffp"),
path('sfp_details/',views.second_year_fee_view,name="sfp"),
path('tfp_details/',views.third_year_fee_view,name="tfp"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_page_view),
path('fourth_details/',views.fourth_year_fee_view,name="fourth"),
    path('profile/',views.student_profile,name="student_profile"),
    path('attendance/',views.student_attendance_view),
path('fee/',views.student_fee_view)
]
