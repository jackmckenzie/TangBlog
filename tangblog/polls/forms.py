from django import forms

from polls.models import Question, Choice

class PollsForm(forms.Form):
    choices = forms.ModelChoiceField(queryset=Choice.objects.all(),widget=forms.RadioSelect(attrs={'id': 'vote-choice', 'required': True}))
    class Meta:
        model = Question
        fields= ['choices']
        self.choices.queryset=Choice.objects.get(pk=2)
