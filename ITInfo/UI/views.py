from django.shortcuts import render,redirect
from django.db import connection
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import plsql_details,plsql_detail_answers
from .forms import  Postformanswer
# Create your views here.
def home(request):

    return render(request,'UI/Base.html')

def plsql(request):
    print('printing the details')
    details=plsql_details.objects.all()
    print('details')
    flag='True'
    return render(request,'UI/plsql.html',{'details':details,'flag':flag})

def question_submit(request):
    Ques=request.POST['question']
    qs=plsql_details(Question=Ques)
    qs.save()
    details = plsql_details.objects.all()
    print(details)
    return render(request, 'UI/plsql.html', {'details': details})

def plsql_answers(request,id):
    #cursor.execute("SELECT Quest FROM plsql_detail_answers where qid={}".format(id))
    #rw = cursor.fetchall()
    #rws=plsql_detail_answers.objects.filter(qid=id).values_list('Quest')[1:]
    #for i in rws:
    #    rw=str(i)
    list=plsql_detail_answers.objects.values_list('qid')
    if (id,) in list:
        objs = plsql_detail_answers.objects.all().filter(qid=id)
        print(objs)
        details = plsql_details.objects.all()
        det = plsql_details.objects.all().filter(id=id)
        return render(request, 'UI/plsql.html', {'details': details, 'objs': objs,'det':det})
    else:
        details = plsql_details.objects.all()
        det = plsql_details.objects.all().filter(id=id)
        return render(request, 'UI/plsql.html', {'details': details,'det':det})



def answer_submit(request,qid):
    #form=Postformanswer()
    #context={
    #    "form":form,
    #}
    #return render(request, 'UI/plsql.html', {'details': details, 'det': det})
    if request.method=='POST':
        ans=request.POST['answer']
        print('-----------')
        print(ans)
        mail=request.POST['email']
        print(mail)
        #ques=plsql_details.objects.all().filter(id=1).values_list('Question')
        #ques=plsql_details.objects.filter(id=1).first()
        detl=plsql_detail_answers(qid=qid,Answ=ans,mail=mail)
        print(detl)
        detl.save()
        objs = plsql_detail_answers.objects.all().filter(qid=qid)
        print(objs)
        details = plsql_details.objects.all()
        det = plsql_details.objects.all().filter(id=qid)
        return render(request, 'UI/plsql.html', {'details': details, 'objs': objs, 'det': det})
    return HttpResponse('<h1>Failure<h1>')



def aboutme(request):
    return render(request,'UI/aboutme.html')


def search(request):
    if request.method=='POST':
        inp=request.POST['inps']
        print('entered in if mainloop')
        print(inp)
        if inp:
            details=plsql_details.objects.filter(Question__contains=inp)
            if details:
                qqid=details[0].id
                objs=plsql_detail_answers.objects.all().filter(qid=qqid)
                det = plsql_details.objects.all().filter(id=qqid)
                return render(request,'UI/plsql.html',{'details':details,'objs':objs,'det':det})
            else:
                print('Entered into else loop')
                nodata='True'
                print(nodata)
                return render(request,'UI/plsql.html',{'nodata':nodata})
    else:
        return render(request,'UI/Base.html')
