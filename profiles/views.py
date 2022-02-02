from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages

# Create your views here.
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(instance, 'Profile Updated Successfully')


    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {
        'orders': orders,
        'form': form,
        'on_profile_page': True,
    }

    return render(request, template, context)
