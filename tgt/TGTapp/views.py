from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
#This is designates the url for the base TGT app
def index(request):
    return render(request, 'TGTapp/index.html')