from django.shortcuts import render, redirect

# Create your views here.
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    students_list = Student.objects.all()
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('students')
    return render(request, 'students.html', {'students': students_list, 'form': form})

def courses(request):
    courses_list = Course.objects.all()
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('courses')
    return render(request, 'courses.html', {'courses': courses_list, 'form': form})

def details(request, student_id):
    student = Student.objects.get(pk=student_id)
    courses_not_registered = Course.objects.exclude(students=student)
    return render(request, 'details.html', {'student': student, 'courses_not_registered': courses_not_registered})
