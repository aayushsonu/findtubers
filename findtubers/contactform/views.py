from django.shortcuts import redirect, render
from .models import ContactForm
from django.contrib import messages
# Create your views here.


def contactform(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        company = request.POST['company']
        subject = request.POST['subject']
        message = request.POST['message']
        phone = request.POST['phone']
        user_id = request.POST['user_id']

        contactform = ContactForm(full_name=full_name, email=email, company=company,
                                  subject=subject, message=message, phone=phone, user_id=user_id)

        contactform.save()

        messages.success(
            request, "Thanks for reaching out to us.We'll contact you soon")
        return redirect("contact")
