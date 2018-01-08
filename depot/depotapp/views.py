#--coding=utf-8
from django.shortcuts import render,get_object_or_404,render_to_response,redirect
from .models import Store,Product,User,Cart,Lineitem
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
#from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm,Store_detail_EditForm,Add_product_Form
import datetime
from django.utils import timezone
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader, RequestContext
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
			user = authenticate(username=username,password=password
			)
			print user
			if user:
				login(request,user)
				if user.is_buyer:
					return redirect(reverse('depotapp:shouye'))
				else:
					print request.user
					print request.user.id
					return redirect(reverse('depotapp:seller_store',args=(user.id,)))
			return render_to_response('login.html',{'loginform':loginform})
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
			choice = registerform.cleaned_data['Is_buyer']
			if choice == 'level1':
				is_buyer=True
			else:
				is_buyer=False
			user_register_time = timezone.now()
			user=User.objects.create_user(username=username,password=password,email=email,Tel =Tel,is_buyer=is_buyer,user_register_time=user_register_time)
			print user.is_buyer
			if user.is_buyer==True:
				return HttpResponse('注册成功')
			else:
				return redirect(reverse('depotapp:seller_store',args=(user.id,)))

			#profile=UserProfile(user_id=user.id,Tel =Tel,is_buyer=is_buyer,user_register_time=user_register_time)
			#profile.save()

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
def product_detail(request,product_id):
	product = get_object_or_404(Product,pk= product_id)
	return render(request,'depotapp/product_detail.html',{'product':product,'user':request.user})
@login_required
def seller_store(request,user_id):
	print user_id
	user = get_object_or_404(User,pk=user_id)
	store_list = user.store_set.all()
	return render_to_response('depotapp/store_list.html',{'store_list':store_list,'user':user})
@login_required
@csrf_exempt
def store_detail_edit(request,store_id):
	print '======================'
	store = get_object_or_404(Store,pk= store_id)
	data = {'store_name':store.store_name,'store_type':store.store_type,'store_addr':store.store_addr,'description':store.description}
	if request.method == 'POST':
		store_form =Store_detail_EditForm(request.POST)
		print store_form.errors,'gagadhah'
		if store_form.is_valid():
			store.store_name = store_form.cleaned_data['store_name']
			store.store_addr = store_form.cleaned_data['store_addr']
			store.description = store_form.cleaned_data['description']
			store.store_type = store_form.cleaned_data['store_type']
			store.save()
			print u'保存成功'
			return redirect(reverse('depotapp:seller_store',args=(store.seller.id,)))
		else:
			print 'wuxiao'
			return render(request,'store_detail_edit.html',{'store':store,'store_form':store_form})
	else:
		store_form = Store_detail_EditForm(initial=data)
		return render(request,'store_detail_edit.html',{'store':store,'store_form':store_form})
@csrf_exempt
@login_required
def add_store(request,user_id):
	store = Store()
	if request.method=='POST':
		store_form =Store_detail_EditForm(request.POST)
		if store_form.is_valid():
			store.store_name = store_form.cleaned_data['store_name']
			store.store_addr = store_form.cleaned_data['store_addr']
			store.description = store_form.cleaned_data['description']
			store.store_type = store_form.cleaned_data['store_type']
			store.store_register_time = timezone.now()
			store.seller = request.user
			store.save()
			print u'添加成功'
			return redirect(reverse('depotapp:seller_store',args=(store.seller.id,)))
		else:
			print 'wuxiao'
			return render(request,'add_store.html',{'store':store,'store_form':store_form})
	else:
		store_form = Store_detail_EditForm()
		return render(request,'add_store.html',{'user':request.user,'store_form':store_form})
@csrf_exempt
@login_required
def add_product(request,store_id):
	store = get_object_or_404(Store, pk=store_id)
	product = Product()
	if request.method=='POST':
		product_form =Add_product_Form(request.POST)
		if product_form.is_valid():
			product.title = product_form.cleaned_data['product_name']
			product.description = product_form.cleaned_data['description']
			product.price = product_form.cleaned_data['price']
			product.time_to_market = timezone.now()
			product.store = store
			product.image_url = 'unsetting'
			product.save()
			print u'添加商品成功'
			return redirect(reverse('depotapp:store_detail',args=(store.id,)))
		else:
			print 'wuxiao'
			return render(request,'add_product.html',{'store':store,'product_form':product_form})
	else:
		product_form = Add_product_Form()
		return render(request,'add_product.html',{'store':store,'product_form':product_form})
@login_required
def store_detail(request,store_id):
	if not request.user.is_buyer:
		store = get_object_or_404(Store, pk=store_id)
		product_list = store.product_set.all().order_by('-time_to_market')
		return render(request,'depotapp/store_detail.html',{'product_list':product_list,'store':store})
	else:
		return HttpResponse('禁止访问')
@login_required
def shopping_cart(request,user_id,product_id):
	user = get_object_or_404(User, pk=user_id)
	if product_id == '0':
		cart = user.cart_set.all()[0]
		print cart
		return render(request, 'shopping_cart.html', {'cart': cart, 'productitem_list': []})
	product = get_object_or_404(Product, pk=product_id)
	if not user.cart_set.all():
		cart =Cart(total_price=0,user=user)
		cart.save()
		lineitem=Lineitem(unit_price=product.price,time_to_cart=timezone.now(),item_price=product.price,pro_item=product)
		lineitem.save()
		lineitem.cart_name.add(cart)
		lineitem.save()
		cart.total_price +=lineitem.item_price
	else:
		cart=user.cart_set.all()[0]
		item=cart.lineitem_set.filter(pro_item=product)
		if item:
			item[0].quantity +=1
			item[0].item_price +=item[0].unit_price
			item[0].save()
			cart.total_price += item[0].unit_price
		else:
			lineitem=Lineitem(unit_price=product.price,time_to_cart=timezone.now(),item_price=product.price,pro_item=product)
			lineitem.save()
			lineitem.cart_name.add(cart)
			lineitem.save()
			cart.total_price +=lineitem.item_price
	cart.save()
	productitem_list = cart.lineitem_set.all()
	return render(request,'shopping_cart.html',{'cart':cart,'productitem_list':productitem_list})
@login_required
def clear_cart(request,user_id,cart_id):
	user = get_object_or_404(User, pk=user_id)
	cart = get_object_or_404(Cart, pk=cart_id)
	items = cart.lineitem_set.all()
	if items:
		for item in items:
			item.delete()
			cart.total_price = 0
			cart.save()
	useless_id = 0
	return redirect(reverse('depotapp:shopping_cart',args=(user.id,useless_id)))
@login_required
def payment(request,user_id,product_id):
	print user_id,'====',product_id
	return HttpResponse('tiaoshi')