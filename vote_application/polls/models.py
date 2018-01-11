#--coding=utf-8
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
	#img = models.ImageField(upload_to='question')
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')#此参数可选。
	def was_published_recently(self):
		now = timezone.now()
		return now >= self.pub_date >= now- datetime.timedelta(days= 1)
	def __unicode__(self):
		return self.question_text#返回unicode
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text #返回utf8
class IMG(models.Model):
	img = models.ImageField(upload_to='img')
	name = models.CharField(max_length=20)