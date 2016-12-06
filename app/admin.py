from django.contrib import admin

# Register your models here.
from .models import Blog,UserProfile
# Register your models here.
admin.site.register(Blog)
admin.site.register(UserProfile)