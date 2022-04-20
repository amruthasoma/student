
from django.urls import path
from crudapp import views

urlpatterns = [
    path('',views.addstudents,name='addstudents'),
    path('addstudentdetails',views.addstudentdetails,name='addstudentdetails'),
    path('showstudent',views.showstudent,name='showstudent'),
    path('editstudent/<int:pk>',views.editstudent,name='editstudent'),
    path('editstu/<int:pk>',views.editstu,name='editstu'),
    path('deletestudent/<int:pk>',views.deletestudent,name='deletestudent'),
    path('delete/<int:pk>',views.delete,name='delete'),
]