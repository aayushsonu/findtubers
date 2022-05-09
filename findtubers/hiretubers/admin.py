from django.contrib import admin
from .models import Hiretuber
# Register your models here.


class Hiretuber_Admin(admin.ModelAdmin):
    def name(self, object):
        return object.first_name + " " + object.last_name

    list_display = (
        'id',
        'name',
        'email',
        'tuber_name'
    )


admin.site.register(Hiretuber, Hiretuber_Admin)
