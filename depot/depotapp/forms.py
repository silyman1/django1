#--coding=utf-8
from django import forms
class LoginForm(forms.Form):
	username = forms.CharField(label='用户名',max_length=50)
	password = forms.CharField(label='密码',widget=forms.PasswordInput())
	#email = forms.EmailField(label='邮箱')
	#Tel = forms.CharField(label='电话',max_length=20)
class RegisterForm(forms.Form):
	username = forms.CharField(label='用户名',max_length=50)
	password = forms.CharField(label='密码',widget=forms.PasswordInput())
	email = forms.EmailField(label='邮箱')
	Tel = forms.CharField(label='电话',max_length=20)