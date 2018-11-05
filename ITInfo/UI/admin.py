from django.contrib import admin

# Register your models here.
from .models import plsql_details,plsql_detail_answers

class plsq_details_layout(admin.ModelAdmin):
    list_display=['id','Question','Answer','Email']

admin.site.register(plsql_details,plsq_details_layout)


class plsql_detail_answers_layout(admin.ModelAdmin):
    list_display=['qid','Quest','Answ','mail']

admin.site.register(plsql_detail_answers,plsql_detail_answers_layout)