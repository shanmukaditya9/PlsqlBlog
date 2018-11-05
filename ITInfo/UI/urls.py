"""ITInfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('plsql/',views.plsql,name='plsql'),
    path('plsql/plsql_answers/<int:id>/',views.plsql_answers,name='answers'),
    path('aboutme/',views.aboutme,name='aboutme'),
    path('answer_submit/<int:qid>/',views.answer_submit,name='answer_submit'),
    path('question_submit/',views.question_submit,name='question_submit'),
    path('search/',views.search,name='search')

]
