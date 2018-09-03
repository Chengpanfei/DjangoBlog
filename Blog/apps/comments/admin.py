from django.contrib import admin
from .models import PostComment,SubComment

# Register your models here.
admin.site.register(PostComment)
admin.site.register(SubComment)