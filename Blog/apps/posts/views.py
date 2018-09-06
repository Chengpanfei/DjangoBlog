from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from .models import Post
from ..categories.models import Category

from .forms import PostForm


from django.contrib.auth.decorators import (
		login_required,
		permission_required
		)
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
@permission_required('Blog.add_post',raise_exception=True)
def post_create(request):
	
	if request.method == 'POST':

		form  = PostForm(request.POST)
		if form.is_valid:


			title = request.POST['title'] 
			body = request.POST['body']
			category = request.POST['category']

			category = get_object_or_404(Category,name=category)
			

			post = Post(title=title,category=category,content=body,author=request.user)

			post.save()
			return redirect('/')
	categories = Category.objects.all()
	return render(request,'posts_create.html',{'categories':categories})
