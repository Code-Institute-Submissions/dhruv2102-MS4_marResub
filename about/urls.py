from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_testimonial, name="about"),
    path("add/", views.add_testimonial, name="add_testimonial"),
    path("edit/<int:testimonial_id>", views.edit_testimonial, name="edit_testimonial"),
    ]
