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
	Choices = (('level1',True),('level2',False))
	Is_buyer = forms.ChoiceField(choices=Choices,label='选择用户类型')
class Store_detail_EditForm(forms.Form):
	store_name = forms.CharField(label='店铺名',max_length=50)
	store_type = forms.CharField(label='店铺类型',max_length=50)
	store_addr = forms.CharField(label='店铺地址',max_length=100)
	description = forms.CharField(label='店铺简介',max_length=100,required=False,widget=forms.Textarea(attrs={'cols':'80','rows':'5'}) )
class Add_product_Form(forms.Form):
	product_name = forms.CharField(label='商品名',max_length=50)
	description = forms.CharField(label='商品简介', max_length=100, required=False,
								  widget=forms.Textarea(attrs={'cols': '80', 'rows': '5'}))
	price = forms.DecimalField(decimal_places=2)
class Recharge_Form(forms.Form):
	amount = forms.DecimalField(decimal_places=2)
class SearchForm(forms.Form):
	search = forms.CharField(label='搜索',max_length=100)
