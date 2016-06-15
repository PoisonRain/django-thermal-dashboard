from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.views import defaults
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login

from .models import Question,Choice
# Create your views here.

def loginResponse(request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse("Success")
			else:
				return HttpResponse("User is disabled.")
		return HttpResponse("Invalid credentials.")

class IndexView(LoginRequiredMixin, generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
	    """Return the last five published questions."""
	    return Question.objects.order_by('-pub_date')[:5]

class DetailView(LoginRequiredMixin, generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(LoginRequiredMixin, generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

@login_required
def allresults(request):
	print get_client_ip(request)
	qs = Question.objects.all()
	return render(request, 'polls/allresults.html', { 'questions' : qs })

@login_required
def vote(request, pk):
	print get_client_ip(request)
	question = get_object_or_404(Question, pk=pk)
	try:
	    selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
	    # Redisplay the question voting form.
	    return render(request, 'polls/detail.html', {
	        'question': question,
	        'error_message': "You didn't select a choice.",
	    })
	else:
	    selected_choice.votes += 1
	    selected_choice.save()
	    # Always return an HttpResponseRedirect after successfully dealing
	    # with POST data. This prevents data from being posted twice if a
	    # user hits the Back button.
	    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
	    ip = x_forwarded_for.split(',')[0]
	else:
	    ip = request.META.get('REMOTE_ADDR')
	return ip
