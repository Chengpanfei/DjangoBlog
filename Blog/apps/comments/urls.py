from django.urls import path
from .views import (
	postComment,
	postSubComment,
	commentBoard,
	)

urlpatterns = [
    path('postComment/', postComment),
    path('postSubComment/', postSubComment),
    path('board/', commentBoard),
]