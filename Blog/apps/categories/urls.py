from django.urls import path
from .views import (
	category_posts
	)

urlpatterns = [
    path('<str:category>/', category_posts),
    path('', category_posts),
]