from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

# Register your models here.


class YtAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="36em"/>'.format(object.photo.url))

    def name(self, object):
        return object.first_name + " " + object.last_name

    list_display = ('id', 'myphoto', 'name', 'subs_count', 'is_featured')
    search_fields = ('first_name', 'last_name', 'camera')
    list_filter = ('city', 'camera_type')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured',)


admin.site.register(Youtuber, YtAdmin)
