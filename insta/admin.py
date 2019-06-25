from django.contrib import admin
from .models import Image,Profile
# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal =('caption')

    admin.site.register(Image)
    admin.site.register(Profile)