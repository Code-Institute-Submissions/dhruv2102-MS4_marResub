from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Testimonials
from .forms import TestimonialsForms

from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    context = {"testimony": testimony}
    return render(request, "about/about.html", context)


@login_required
def add_testimonial(request):
    """
    View to add Testimonial
    """
    if not request.user.is_superuser:
        messages.error(request, "Only super users can do that")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = TestimonialsForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfull added testimonial!")
            return redirect(reverse('about'))
        else:
            messages.error(
                request, "Failed to add testimonial. \
                    Please ensure for is valid")

    form = TestimonialsForms()
    template = "about/add_testimonial.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def edit_testimonial(request, testimonial_id):
    """
    View to edit Testimonial
    """
    if not request.user.is_superuser:
        messages.error(request, "Only super users can do that")
        return redirect(reverse("home"))

    testimonial = get_object_or_404(Testimonials, pk=testimonial_id)
    if request.method == "POST":
        form = TestimonialsForms(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfull edited testimonial!")
            return redirect(reverse('about'))
        else:
            messages.error(
                request, "Failed to add testimonial. \
                    Please ensure for is valid")

    form = TestimonialsForms(instance=testimonial)
    messages.info(request, f"You are editing the testimonial by {testimonial}")

    template = "about/edit_testimonial.html"
    context = {
        "form": form,
        "testimonial": testimonial,
    }
    return render(request, template, context)


@login_required
def delete_testimonial(request, testimonial_id):
    """
    View to delete Testimonial
    """
    if not request.user.is_superuser:
        messages.error(request, "Only super users can do that")
        return redirect(reverse("home"))

    testimonial = get_object_or_404(Testimonials, pk=testimonial_id)
    testimonial.delete()
    messages.success(request, "Testimonial deleted!")
    return redirect(reverse("about"))
