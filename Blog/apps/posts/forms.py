from django import forms

class PostForm(forms.Form):
	title = forms.CharField()
	body = forms.CharField()
	category = forms.CharField()
	body_type = forms.CharField() # html 或者 markdown