from django.urls import path
from .views import (
	post_content
	)

urlpatterns = [
    path('<int:post_id>/', post_content),
]