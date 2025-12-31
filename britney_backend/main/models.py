
# Create your models here.
from django.db import models

class IPLog(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} @ {self.created_at}"
    