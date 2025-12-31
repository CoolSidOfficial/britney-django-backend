from django.http import JsonResponse
from .models import IPLog

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

def log_ip(request):
    ip = get_client_ip(request)
    user_agent = request.META.get("HTTP_USER_AGENT", "")

    IPLog.objects.create(
        ip_address=ip,
        user_agent=user_agent
    )

    return JsonResponse({"status": "ok"})

































