from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone
from ..categories.models import Category,Tag

# Create your models here.
# class PostManager(models.Mangager):
# 	"""博客模型管理器，除去id为1博文，该博文作为留言板内容"""
# 	def get_query_set(self):
# 		superclass = super(PostManager,self)
# 		return superclass.get_query_set().filter(id > 1)
		
#定义博客模型
class Post(models.Model):
	#博客标题
	title = models.CharField(max_length = 100)
	#博客内容
	content = models.TextField()
	#博客创建时间
	create_time = models.DateTimeField(default = timezone.now)
	#博客的作者
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	#记录博客的点击量
	click_num = models.IntegerField(default=0)
	#博客的分类，一对多关系，外键约束
	category = models.ForeignKey(Category,related_name='posts',default=1,on_delete=models.CASCADE)
	#博客的标签，多对多关系
	tags = models.ManyToManyField(Tag,related_name='posts')

	#定义文字描述
	def __str__(self):
		return self.author.username + ':' + self.title