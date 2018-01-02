from django.contrib import admin

# Register your models here.
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):#StackedInline
	model = Choice
	extra = 3
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	('Question',{'fields':['question_text']}),
	('Date information',{'fields':['pub_date'],'classes':['collapse']}),
]
	inlines = [ChoiceInline]
	list_display = ('question_text','pub_date','was_published_recently')
	list_filter = ['pub_date']
admin.site.register(Question,QuestionAdmin)
#admin .site.register(Choice)