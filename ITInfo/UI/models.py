from django.db import models
from django.urls import reverse

# Create your models here.

class plsql_details(models.Model):
    Question=models.TextField(max_length=1000)
    Answer=models.TextField(max_length=10000)
    Email=models.EmailField()

    def __str__(self):
        return self.Question

    def get_absolute_url(self):
        print('hitted first one')
        return reverse("answers",kwargs={'id':self.id})

class plsql_detail_answers(models.Model):
    qid=models.IntegerField()
    Quest=models.TextField(max_length=1000)
    Answ=models.TextField(max_length=10000)
    mail=models.EmailField()

    def __str__(self):
        return self.Answ
    #
    # def get_absolute_url(self):
    #     print('hitted second one')
    #     return reverse("answer_submit",kwargs={'qid':self.qid})


