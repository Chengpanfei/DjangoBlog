from django.shortcuts import render
from django.db.models import Count
from ..posts.models import Post
# Create your views here.


def home(request):
	'''
	博客网站首页视图
	'''
	#按照时间排序，取最近3个博文
	lasted_posts = Post.objects.all().order_by('-create_time')[0:3]
	#按照拥有的评论数目排序，聚合后的结果作为属性
	hot_posts = Post.objects.annotate(comment_num=Count('comments')).order_by('-comment_num')[0:3]


	#往模板中传递的上下文
	context = {
		'lasted_posts':lasted_posts,
		'hot_posts':hot_posts,
	}
	return render(request,'home.html',context)

def about(request):
	'''
	关于页面
	'''
	return render(request,'about.html')
