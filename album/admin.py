from django.contrib import admin
from .models import Location, Image, Category

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('image_category',)

admin.site.register(Location)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category)