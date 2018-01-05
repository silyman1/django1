#--coding=utf-8
from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser,models.Model):
	#user_name = models.CharField(max_length=100,unique=True)
	#password = models.SlugField(max_length=6)
				#user=models.OneToOneField(User,unique=True,verbose_name=('用户'))
	user_register_time = models.DateTimeField('date to register',auto_now_add=True)
	is_buyer = models.NullBooleanField()
	Tel = models.CharField(max_length=20,blank=True)
	def __unicode__(self):
		return self.username#返回unicode
class Store(models.Model):
	store_name = models.CharField(max_length=100,unique=True)
	store_type = models.CharField(max_length=100)
	store_addr = models.CharField(max_length=200)
	description=models.TextField()
	store_register_time = models.DateTimeField('date to register')
	store_product_num = models.PositiveIntegerField(default = 0)
	seller = models.ForeignKey(User)
	def __unicode__(self):
		return self.store_name#返回unicode
class Product(models.Model):
	title = models.CharField(max_length=100)
	description=models.TextField()
	image_url = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=8,decimal_places=2)
	time_to_market =models.DateTimeField('date to market')
	store = models.ForeignKey(Store)
	def __unicode__(self):
		return self.title#返回unicode