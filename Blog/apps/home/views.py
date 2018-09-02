from django.shortcuts import render
from ..posts.models import Post
# Create your views here.


def home(request):
	'''
	博客网站首页视图
	'''

	posts = Post.objects.all()[1:]

	#往模板中传递的上下文
	context = {
		'posts':posts
	}
	return render(request,'home.html',context)
