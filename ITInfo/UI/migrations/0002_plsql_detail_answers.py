# Generated by Django 2.1.2 on 2018-10-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='plsql_detail_answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qid', models.IntegerField()),
                ('Quest', models.TextField(max_length=1000)),
                ('Answ', models.TextField(max_length=10000)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
