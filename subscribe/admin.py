from django.contrib import admin
from .models import Subscribers

# Register your models here.
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("email",)


admin.site.register(Subscribers, SubscribeAdmin)
