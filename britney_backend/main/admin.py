from django.contrib import admin
from .models import IPLog
# Register your models here.

@admin.register(IPLog)
class IPLogAdmin(admin.ModelAdmin):
    list_display = ("ip_address", "created_at")
    list_filter = ("created_at",)
    search_fields = ("ip_address",)
