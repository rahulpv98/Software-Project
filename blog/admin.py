from django.contrib import admin
from .models import Post, Comment

# Register your models here.
from .models import Post

admin.site.register(Post)
#superuser username:admin, password:sivabara

admin.site.register(Comment)

