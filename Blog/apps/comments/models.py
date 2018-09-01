from django.db import models
from django.contrib.auth.models import User
from ..posts.models import Post
# Create your models here.


class PostComment(models.Model):
	'''
		博客评论模型
		评论对象与用户和博客都是一对多关系，
		这里使用外键进行约束
	'''
	#发表评论的用户
	author = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
	#评论对应的博客
	post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
	#评论内容
	content = models.TextField()
	#评论发表时间
	create_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.author.username + '->' + self.post.title


class SubComment(models.Model):
	'''
		采用两级评论模型，二级评论显示为楼中楼
	'''
	#发表评论的用户
	author = models.ForeignKey(User,related_name='send_comments',on_delete=models.CASCADE)
	#该评论的接收用户
	dest_user = models.ForeignKey(User,related_name='received_comments',on_delete=models.CASCADE)
	#该评论的父级评论
	post_comment = models.ForeignKey(PostComment,related_name='subcomments',on_delete=models.CASCADE)
	#评论内容
	content = models.TextField()
	#评论发表时间
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.author.username + '->' + self.dest_user.username