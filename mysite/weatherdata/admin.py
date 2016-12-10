from django.contrib import admin
from .models import Post
from .models import Weather

admin.site.register(Post)
admin.site.register(Weather)
