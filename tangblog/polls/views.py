from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import json
from django.utils import timezone

from .forms import PollsForm
from .models import Question, Choice


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['form'] = PollsForm(qid=[i for i in filter(None, self.request.path_info.split('/'))][-1])
        return context

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be published in the future).
        """
        return Question.objects.filter(
                    pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]

class ResultsView(generic.DetailView):
    model = Question

#def vote(request, question_id):
#    p = get_object_or_404(Question, pk=question_id)
#    try:
#        selected_choice = p.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        return render(request, 'polls/detail.html', {
#            'question': p,
#            'error_message': "You didn't select a choice",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        if request.method == 'POST':
#            return HttpResponse(json.dumps(selected_choice), context_type="application/json")
#        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
def vote(request):
    if request.method == "POST":
        vote_value = request.POST.get('the_vote')
        question_id = request.POST.get('question_id')
        print(vote_value)
        print(question_id)
        response_data = {}


        q = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = q.choice_set.get(pk=vote_value)
        except(KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': q,
                'error_message': "You didn select a choice",
                })
        else:
            selected_choice.votes += 1
            selected_choice.save()

            results = q.choice_set.all()
            response_data['results'] = results

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
