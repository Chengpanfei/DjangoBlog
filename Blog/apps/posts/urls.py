from django.urls import path
from .views import (
	post_content,
	post_create,
	uploadImage,
	archives,
	tags,
	)

urlpatterns = [
    path('<int:post_id>/', post_content),
    path('create/',post_create),
    path('uploadImage/',uploadImage),
    path('archives/<year>/<month>/',archives),
    path('tags/<tag>/',tags),
]