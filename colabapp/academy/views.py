from django.shortcuts import render
from .models import Course

# Create your views here.

def v_index(request):
    context = {
        'course1' : Course.objects.get(name = 'Matematica Avanzada'),
        'course2' : Course.objects.get(name = 'Literatura'),
    }
    return render(request, 'index.html',context)

def v_course(request, course_id):
    context = {}
    return render(request, 'course.html', context)