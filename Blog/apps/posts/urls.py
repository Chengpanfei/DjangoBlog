from django.urls import path
from .views import (
	post_content,
	post_create,
	)

urlpatterns = [
    path('<int:post_id>/', post_content),
    path('create/',post_create),
]