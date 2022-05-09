from django.shortcuts import redirect, render
from .models import Hiretuber
from django.contrib import messages

# Create your views here.


def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        message = request.POST['message']
        phone = request.POST['phone']
        user_id = request.POST['user_id']

        # TODO: do all sanitization

        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name,
                              email=email, city=city, state=state, message=message, phone=phone, user_id=user_id)

        hiretuber.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('youtubers')
