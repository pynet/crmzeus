from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')


def report(request):
    return render(request, 'core/report.html')
