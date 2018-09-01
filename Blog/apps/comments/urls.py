from django.urls import path
from .views import (
	postComment,
	postSubComment,
	)

urlpatterns = [
    path('postComment/', postComment),
    path('postSubComment/', postSubComment),
]