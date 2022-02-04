from django.contrib import admin
from .models import Testimonials

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'testimony',
    )


admin.site.register(Testimonials, TestimonialAdmin)