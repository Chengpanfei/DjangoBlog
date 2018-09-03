
from django import forms


class RegisterForm(forms.Form):
	'''
	用户注册表格
	'''
	name = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget = forms.PasswordInput)
	password2 = forms.CharField(widget = forms.PasswordInput)
	#captcha = CaptchaField()

class LoginForm(forms.Form):
	'''
	用户登录表格
	'''
	email = forms.EmailField()
	password = forms.CharField(widget = forms.PasswordInput)
	#captcha = CaptchaField()