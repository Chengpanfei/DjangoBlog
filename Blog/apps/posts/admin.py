from django.contrib import admin
from .models import Post

# Register your models here.
#定制管理内容
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','create_time')

#在管理中注册模型
admin.site.register(Post,PostAdmin)