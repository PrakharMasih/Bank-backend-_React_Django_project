from django.http import HttpResponse

def home(rquest):
    return HttpResponse("home page")