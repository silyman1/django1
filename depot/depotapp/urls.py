from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$',views.index,name='index'),
				url(r'^shouye/$',views.shouye,name='shouye'),
				url(r'^regist/$',views.register,name='regist'),
				url(r'^(?P<product_id>[0-9]+)/$',views.detail,name='detail'),
				url(r'^seller/$',views.seller_list,name='seller'),
]