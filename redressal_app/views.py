from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# HttpResponseRedirect, Http404, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, 
# HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseGone, HttpResponseNotModified, 
# HttpResponsePermanentRedirect, HttpResponseTemporaryRedirect, HttpResponseNotModified


# Create your views here.

def home(request):
    return render (request, 'index.html') 

def navbar_home(request):
    return render (request, 'navbar_home.html')

def login(request):
    return render (request, 'login.html')
