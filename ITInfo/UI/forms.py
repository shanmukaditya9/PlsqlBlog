from django import forms
from .models import plsql_detail_answers,plsql_details

class Postformanswer(forms.ModelForm):
    class Meta:
        model= plsql_detail_answers
        fields=[
            'qid','Quest','Answ','mail'
        ]
