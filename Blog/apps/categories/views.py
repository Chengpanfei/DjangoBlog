from django.shortcuts import render,get_object_or_404
from .models import Category
from ..posts.models import Post
from ...libs.paginator import paginate

# Create your views here.
def category_posts(request,category=''):
	'''
	用于根据分类显示博客列表的视图
	'''
	if category == '':
		#显示全部博客
		posts = Post.objects.all()[1:]
	else:
		#查找分类对应的全部博客
		category_obj = get_object_or_404(Category,name=category)
		posts = category_obj.posts.all()

	#对posts分页处理
	page = request.GET.get('page')
	posts = paginate(
		objects = posts,
		current_page = page,
		num_per_page= 5
		)
	#用于显示全部分类列表
	categories = Category.objects.all()

	context = {
		'posts':posts,
		'categories':categories,
		'category':category,
	}

	return render(request,'category.html',context)