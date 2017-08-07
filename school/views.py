from django.shortcuts import render

# Create your views here.
from .models import Student
from .permission import check_permission

@check_permission
def students(request):
    print('ddeee')
    students=Student.objects.all()
    return render(request,'students_list.html',locals())
