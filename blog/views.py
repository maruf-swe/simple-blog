from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1></h1>')

def about(request):
    return HttpResponse('<h1></h1>')
