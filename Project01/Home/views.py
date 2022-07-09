from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home Page")
def about(request):
    return HttpResponse("this is about Page")
def contact(request):
    return HttpResponse("this is contact Page")
def services(request):
    return HttpResponse("this is services Page")
