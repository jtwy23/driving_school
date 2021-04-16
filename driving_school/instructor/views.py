from django.shortcuts import render


def home_instructor(request):
    return render(request, 'index_instructor.html')