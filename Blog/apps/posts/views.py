from django.shortcuts import (
	render,
	redirect,
	get_object_or_404
	)
from django.http import Http404, HttpResponse
from .models import Post
from ..categories.models import Category

import json

from .forms import PostForm


from django.contrib.auth.decorators import (
	login_required,
	permission_required
	)

from django.views.decorators.http import require_POST

from ...libs.uploads import save_img_to_cos

from ...libs.paginator import paginate
# Create your views here.

def post_content(request,post_id):
	'''
		博客内容视图
		当前为接收一个id号，查找对应博客内容
	'''
	if post_id == 1:
		#post_id为1代表留言板
		return redirect('/commentBoard/')

	post = get_object_or_404(Post,pk=post_id)

	#每次访问点击量加1
	post.click_num += 1
	post.save()

	context = {
		'post':post,
	}

	return render(request,'post_content.html',context)


'''
先判断是否登录，若没有登录将会重定向到登录页面
再判断是否有相关权限，若没有将返回403 Forbidden
'''
@login_required(login_url='/users/login/')
@permission_required('posts.add_post',raise_exception=True)
def post_create(request):
	'''
	创建博客视图
	'''
	if request.method == 'POST':

		form  = PostForm(request.POST)
		if form.is_valid:


			title = request.POST['title'] 
			body = request.POST['body']
			category = request.POST['category']

			category = get_object_or_404(Category,name=category)
			

			post = Post(title=title,category=category,content=body,author=request.user)

			post.save()
			return redirect('/posts/' + str(post.id))

	categories = Category.objects.all()
	return render(request,'posts_create.html',{'categories':categories})


@require_POST
@login_required(login_url='/users/login/')
def uploadImage(request):

	'''
	接收用户上传的图片，并保存至腾讯云对象存储
	'''
	filename = save_img_to_cos(request.FILES.get('img'),
		request.user.id)
	
	result = {
		"errno": 0,
		"data": [filename,
		]

	}
	return HttpResponse(json.dumps(result),
		content_type="application/json")


def archives(request, year, month):
	'''
	博客归档视图
	'''
	

	posts = Post.objects.filter(
		create_time__year=year,
		create_time__month=month,
		).order_by('-create_time')




	page = request.GET.get('page')

	posts = paginate(
		objects = posts,
		current_page = page,
		num_per_page= 5
		)
	
	context = {
		'posts':posts
	}
	return render(request, 'archives.html',context)


