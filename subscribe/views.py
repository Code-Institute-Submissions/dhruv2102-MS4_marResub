from django.shortcuts import render


def subscribe(request):
    """
    Subscribe view
    """
    template = 'subscribe/subscribe.html'
    return render(request, template)