from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("service", views.service, name="service"),
    path("project", views.project, name="project"),
    path("contact", views.contact, name="contact"),
    path("404", views.notFound, name="notFound"),
    path("testimonial", views.testimonial, name="testimonial"),
    path("team", views.team, name="team")

]