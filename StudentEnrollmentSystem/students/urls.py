from django.urls import path,include
from .import views

urlpatterns = [
   
    path("",views.home,name="HomePage"),
    path("addstudent/",views.addStudent,name="Student Form"),
    path("viewstudents/",views.viewstudents,name="View Students"),
    path("viewstudents/<int:id>/",views.student,name="View Students"),
    path("getdistrict/",views.getdistrict,name="getdistrict"),
]

