from django.shortcuts import render

# Create your views here.

def index(request):
    return(render(request, "index.html"))


def about(request):
    return(render(request, "about.html"))


def service(request):
    return(render(request, "service.html"))


def project(request):
    return(render(request, "project.html"))


def contact(request):
    return(render(request, "contact.html"))


def notFound(request):
    return(render(request, "404.html"))


def testimonial(request):
    return(render(request, "testimonial.html"))


def team(request):
    return(render(request, "team.html"))