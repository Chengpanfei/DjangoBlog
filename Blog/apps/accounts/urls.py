from django.urls import path
from .views import (
	user_register,
	user_login,
	user_logout,
	)

urlpatterns = [
    path('register/', user_register),
    path('login/', user_login),
    path('logout/', user_logout),
]