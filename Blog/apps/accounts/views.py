from django.shortcuts import render,redirect 

from .forms import (
	RegisterForm,
	LoginForm,
	)

from django.contrib.auth import (
	authenticate,
	login,
	logout,
	)

from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def user_register(request):
	'''
	用户注册视图
	'''
	if request.method == 'POST':

		form = RegisterForm(request.POST)

		if form.is_valid():
			data = form.cleaned_data

			form_name = data['name']
			form_email = data['email']
			form_password = data['password']
			form_password2 = data['password2']

			user = User.objects.filter(email = form_email).first()
			
			if user:
				#返回user不为空，该邮箱已被注册
				messages.add_message(request,messages.ERROR,'你已经注册过了！')

			elif form_password != form_password2:
				#两次输入密码不一致
				messages.add_message(request,messages.ERROR,'两次输入密码不一致！')
			else:
				#创建新用户
				user = User.objects.create_user(
					username = form_name, 
					email = form_email,
					password = form_password
					)
				user.save()

				msg = '恭喜你，' + form_name +' 注册成功，登录后即可发表评论！'
				messages.add_message(request,messages.ERROR,msg)

				#重定向至首页
				return redirect('/')
		
		else:
			#表格验证不通过，验证码输入有误
			messages.add_message(request,messages.ERROR,'验证码输入有误！')
	
	form = RegisterForm()

	return render(request,'register.html',{'form':form})



def user_login(request):
	'''
	用户登录视图
	'''
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			data = form.cleaned_data

			form_email = data['email']
			form_password = data['password']

			#在数据库中查询
			user = User.objects.filter(email = form_email).first()

			
			if not user:
				#未在数据库中查询到
				messages.add_message(request,messages.ERROR,'该账号尚未注册！')
			

			elif authenticate(request, username = user.username,password=form_password):
				#暂时使用用户名和密码判断是否登录成功，
				#原则上应该使用邮箱和密码判断，后期改进
				#查询到用户，并且验证密码正确
				msg = '恭喜你，'+user.username +' 登录成功，你的Email：' + user.email
				messages.add_message(request,messages.INFO,msg)
				login(request,user)
				return redirect('/')
			
			else:
				#验证密码错误
				messages.add_message(request,messages.ERROR,'账号或密码输入有误！')
		
		else:
			#验证码输入有误
			messages.add_message(request,messages.ERROR,'验证码输入有误！')
	
	form = LoginForm()#登录表单
	return render(request,'login.html',{'form':form})


def user_logout(request):
	'''
	用户退出登录视图
	'''
	messages.add_message(request,messages.INFO,'退出登录成功！')
	logout(request)
	return redirect('/')