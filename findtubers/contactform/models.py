from django.db import models
from datetime import datetime


class ContactForm(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    company = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)
    phone = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.full_name
