from django.shortcuts import render
from .models import Testimonials
# Create your views here.


def about(request):
    """
    Returns about page
    """
    return render(request, "about/about.html")


def get_testimonial(request):
    """
    View to get testimonial
    """
    testimony = Testimonials.objects.all()
    context = {
        "testimony": testimony
    }
    return render(request, 'about/about.html', context)