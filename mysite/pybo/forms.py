from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '일정 추가',
        }

class ScheduleForm(forms.Form):
    subject = forms.CharField(label='일정 제목', max_length=100)
    schedule_date = forms.DateField(label='일정 날짜', widget=forms.DateInput(attrs={'type': 'date'}))
    content = forms.CharField(label='일정 내용', widget=forms.Textarea)