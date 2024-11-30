from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def student_list(request):
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        email = request.GET.get('email')
        date_birth = request.GET.get('date_birth')
        gender = request.GET.get('gender')
        address = request.GET.get('address')
        if first_name is not None and last_name is not None and email is not None and date_birth is not None and gender is not None and address is not None:

            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date_birth=date_birth,
                gender=gender,
                address=address
            )


        student = Student.objects.all()
        ctx = {'students': student}
        return render(request, 'students/students-list.html', ctx)