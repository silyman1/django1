from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question,Choice,IMG
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
#from django.template import RequestContext,loader
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	def get_queryset(self):
		return	Question.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
	#question = get_object_or_404(Question,pk = question_id)
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("question does not exist !!!")
	#return render(request,'polls/detail.html',{'question':question})
	model = Question
	template_name= 'polls/detail.html'
class ResultsView(generic.DetailView):
	#print '============================'
	#question = get_object_or_404(Question,pk = question_id)
	#print question
	#return render(request,'polls/results.html',{'question':question})
	model = Question
	template_name = 'polls/results.html'
def vote(request, question_id):
	p =get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{'question':p,'error_message':"YOU didn't select any choice.."})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		a = reverse('polls:results',args=(p.id,))
		print a,'#################'
		return HttpResponseRedirect(a)
@csrf_exempt
def uploadImg(request):
	if request.method == 'POST':
		new_img = IMG(
			img=request.FILES.get('img'),
			name = request.FILES.get('img').name
		)
		new_img.save()
	return render(request, 'polls/uploadimg.html')
@csrf_exempt
def showImg(request):
	imgs = IMG.objects.all()
	urls =[]
	for img in imgs:
		url =img.img.url.encode('utf-8')
		urls.append(url)
	content = {
		'urls':urls,
	}
	for i in imgs:
		print i.img.url.encode('utf-8')
	return render(request, 'polls/showimg.html',content)