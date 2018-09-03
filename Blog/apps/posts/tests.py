from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.
class PostsTest(TestCase):

	def test_magic_str(self):

		user = User(username="test");
		user.save()

		post = Post(title="My first post!",content="nothing!",author=User.objects.first())
		post.save()
		
		self.assertEqual(str(post),"test:My first post!")
