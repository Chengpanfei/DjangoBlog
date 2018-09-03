from django import forms

class CommentForm(forms.Form):
	content = forms.CharField()
	post_id = forms.CharField()

class SubCommentForm(forms.Form):
	content = forms.CharField()
	post_comment_id = forms.CharField()
	dest_id = forms.CharField()