from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from .models import Post
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