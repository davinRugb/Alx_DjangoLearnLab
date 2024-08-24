from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello! wass GOOD")

def about(request):
    return HttpResponse("my About page")