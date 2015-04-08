from django import forms

from polls.models import Question, Choice

class PollsForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('pub_date', 'question_text',)
    def __init__(self, *args, **kwargs):
        qid = kwargs.pop('qid')
        super(PollsForm, self).__init__(*args, **kwargs)
        q = Question.objects.get(id=qid)
        self.fields['choice_set'] = forms.ModelChoiceField(queryset=q.choice_set.all(),widget=forms.RadioSelect(attrs={'id': 'vote-choice', 'required': True}),label='')
