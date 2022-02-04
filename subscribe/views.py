from django.shortcuts import render
from django.contrib import messages

from .forms import SubscribeForm


def subscribe(request):
    """
    Subscribe view
    """
    template = "subscribe/subscribe.html"
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubscribeForm()
            messages.success(request, "Successfully subscribed!")
        else:
            messages.error(request, "Failed to subscribe!")
    else:
        form = SubscribeForm()

    context = {
        "form": form,
    }
    return render(request, template, context)
