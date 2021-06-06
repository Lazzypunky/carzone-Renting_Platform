from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'thumbnail' ,'car_title' , 'color','is_featured' , 'created_date')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_filter = ('color',)
    list_editable = ('is_featured',)

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Photo'
    
admin.site.register(Car, CarAdmin)
