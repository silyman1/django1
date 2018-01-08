from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$',views.index,name='index'),
				url(r'^shouye/$',views.shouye,name='shouye'),
				url(r'^regist/$',views.register,name='regist'),
				url(r'^product/(?P<product_id>[0-9]+)/$',views.product_detail,name='product_detail'),
				url(r'^seller/$',views.seller_list,name='seller'),
				url(r'^seller/(?P<user_id>[0-9]+)/seller_store/$',views.seller_store,name='seller_store'),
				url(r'^store/(?P<store_id>[0-9]+)/edit/$',views.store_detail_edit,name='store_detail_edit'),
				url(r'^seller/(?P<user_id>[0-9]+)/add_store/$',views.add_store,name='add_store'),
				url(r'^store/(?P<store_id>[0-9]+)/add_product/$',views.add_product,name='add_product'),
				url(r'^store/(?P<store_id>[0-9]+)/detail/$',views.store_detail,name='store_detail'),
				url(r'^buyer/(?P<user_id>[0-9]+)/shopping_cart/(?P<product_id>[0-9]+)/$',views.shopping_cart,name='shopping_cart'),
				url(r'^buyer/(?P<user_id>[0-9]+)/payment/(?P<product_id>[0-9]+)/$',views.payment,name='payment'),
				url(r'^buyer/(?P<user_id>[0-9]+)/clear/(?P<cart_id>[0-9]+)/$',views.clear_cart,name='clear_cart'),
]