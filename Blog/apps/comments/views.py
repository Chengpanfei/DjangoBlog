from django.shortcuts import render,get_object_or_404 ,redirect

from django.contrib.auth.decorators import (
	login_required,
	permission_required
	)

from django.views.decorators.http import require_POST

from ..posts.models import Post
from .models import PostComment,SubComment
from .froms import CommentForm,SubCommentForm

from django.contrib.auth.models import User
# Create your views here.

@require_POST
@login_required(login_url='/users/login/')
def postComment(request):
	'''
		处理评论内容的视图
	'''
	form = CommentForm(request.POST)
	if form.is_valid:

		post_id = request.POST['post-id']
		content = request.POST['content']

		post = get_object_or_404(Post,pk=int(post_id))

		comment = PostComment(author=request.user,post=post,content=content)
		comment.save()

		if int(post_id) != 1:
			'''
				post_id为1代表的是留言板内容
			'''
			return redirect('/posts/' + post_id)

	return redirect('/commentBoard/') 


@require_POST
@login_required(login_url='/users/login/')
def postSubComment(request):

	form = SubCommentForm(request.POST)

	if form.is_valid:

		content = request.POST['content']
		post_comment_id = int(request.POST['post-comment-id'])
		dest_id = int(request.POST['dest-id'])

		post_comment = get_object_or_404(PostComment,pk=post_comment_id)

		dest = get_object_or_404(User,pk=dest_id)

		subcomment = SubComment(author=request.user,dest_user=dest,post_comment=post_comment,content=content)
		subcomment.save()

		post_id = post_comment.post.id;

		if post_id != 1:
			return redirect('/posts/' + str(post_id))

	return redirect('/commentBoard/') 