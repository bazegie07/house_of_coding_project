from django.shortcuts import render

def index(request):
    return render (request,'courses/courses.html')

def course(request):
    return render (request,'courses/course.html')

def search(request):
    return render (request,'courses/search.html')


course

search
