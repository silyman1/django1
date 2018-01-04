#--coding=utf-8
from django.shortcuts import render,get_object_or_404,render_to_response,redirect
from .models import Store,Product,User
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
#from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm
import datetime
from django.utils import timezone
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.
@csrf_exempt
def login_view(request):
	#网上为username=request.POST['username'],不可用
	#user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
	#if user is not None:
	#	login (request,user)
	#	print request.user
	#	return index(request)
	#else:
	if request.method == 'POST':
		loginform = LoginForm(request.POST)
		if loginform.is_valid():
			username =loginform.cleaned_data['username']
			password =loginform.cleaned_data['password']
			#user = User.objects.filter(username__exact=username,password__exact=password)
			user = authenticate(username=username,password=password)
			print user
			if user:
				login(request,user)
				if user.is_buyer:
					return redirect(reverse('depotapp:shouye'))
				else:
					print request.user
					return redirect(reverse('depotapp:seller'))
	else:
		loginform = LoginForm()
		return render_to_response('login.html',{'loginform':loginform})
def logout_view(request):
	logout(request)
	return redirect(reverse('depotapp:index'))
@csrf_exempt
def register(request):
	if request.method == 'POST':
		registerform = RegisterForm(request.POST)
		if registerform.is_valid():
			username = registerform.cleaned_data['username']
			password = registerform.cleaned_data['password']
			email  =registerform.cleaned_data['email']
			Tel =registerform.cleaned_data['Tel']
			is_buyer = False
			user_register_time = timezone.now()
			user=User(username=username,password=password,email=email,Tel =Tel,is_buyer=is_buyer,user_register_time=user_register_time)
			user.save()
			#profile=UserProfile(user_id=user.id,Tel =Tel,is_buyer=is_buyer,user_register_time=user_register_time)
			#profile.save()
			return HttpResponse('注册成功')
	else:
		registerform =RegisterForm()
	return render_to_response('regist.html',{'registerform':registerform,'title':'注册啦啦啦'})
@login_required
def shouye(request):
	print request.user
	product_list = Product.objects.order_by('-time_to_market')[:20]
	return render(request,'depotapp/shouye.html',{'product_list':product_list})
@login_required
def seller_list(request):
	print request.user,'aaa'
	if not request.user.is_buyer:
		product_list = Product.objects.order_by('-time_to_market')[:20]
		return render(request,'depotapp/seller_list.html',{'product_list':product_list})
	else:
		return HttpResponse('禁止访问')
def index(request):
	product_list = Product.objects.order_by('-time_to_market')[:20]
	return render(request,'depotapp/index.html',{'product_list':product_list})
def detail(request,product_id):
	product = get_object_or_404(Product,pk= product_id)
	return render(request,'depotapp/detail.html',{'product':product})
