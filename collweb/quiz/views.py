from django.shortcuts import render
from quiz.models import *
from quiz.forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from insert import insertion
from django.core import serializers
from django.http import JsonResponse
from . import forms
import json
from quiz.serializing import LazyEncoder
# from django.views.decorators.csrf import csrf_exempt


def java_login(request):
    form = java_form()
    reg=[]
    regno = java_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    if request.method =='POST':
        form = java_form(request.POST)
        if form.is_valid():
            # for i in range(len(reg)):
            #     if form.cleaned_data['regno'] == reg[i]:
            #
            #         return HttpResponse('<h1>Already attended the quiz Come Back Later</h1>')
            #     else:
                    # if dbms_score.objects.count() > 10:
                    #     object = dbms_questions.objects.oldest()
                    #     object[0].delete()
                    form.save(commit =True)
                    return render(request,'quiz/java_quiz.html')
        else:
            print('ERROR FORM INVALID')
    return render(request,'quiz/java_login.html',{'form':form})

def vb_login(request):
    form = vb_form()
    reg=[]
    regno = vb_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    if request.method =='POST':
        form = vb_form(request.POST)
        if form.is_valid():
            # for i in range(len(reg)):
            #     if form.cleaned_data['regno'] == reg[i]:
            #
            #         return HttpResponse('<h1>Already attended the quiz Come Back Later</h1>')
            #     else:
                    # if dbms_score.objects.count() > 10:
                    #     object = dbms_questions.objects.oldest()
                    #     object[0].delete()
                    form.save(commit =True)
                    return render(request,'quiz/vb_quiz.html')
        else:
            print('ERROR FORM INVALID')
    return render(request,'quiz/vb_login.html',{'form':form})



def ca_login(request):
    form = ca_form()
    reg=[]
    regno = ca_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    if request.method =='POST':
        form = ca_form(request.POST)
        if form.is_valid():
            # for i in range(len(reg)):
            #     if form.cleaned_data['regno'] == reg[i]:
            #
            #         return HttpResponse('<h1>Already attended the quiz Come Back Later</h1>')
            #     else:
                    # if dbms_score.objects.count() > 10:
                    #     object = dbms_questions.objects.oldest()
                    #     object[0].delete()
                    form.save(commit =True)
                    return render(request,'quiz/ca_quiz.html')
        else:
            print('ERROR FORM INVALID')
    return render(request,'quiz/ca_login.html',{'form':form})


def os_login(request):
    form = os_form()
    reg=[]
    regno = os_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    if request.method =='POST':
        form = os_form(request.POST)
        if form.is_valid():
            # for i in range(len(reg)):
            #     if form.cleaned_data['regno'] == reg[i]:
            #
            #         return HttpResponse('<h1>Already attended the quiz Come Back Later</h1>')
            #     else:
                    # if dbms_score.objects.count() > 10:
                    #     object = dbms_questions.objects.oldest()
                    #     object[0].delete()
                    form.save(commit =True)
                    return render(request,'quiz/os_quiz.html')
        else:
            print('ERROR FORM INVALID')
    return render(request,'quiz/os_login.html',{'form':form})



def cpp_login(request):
    form = cpp_form()
    reg=[]
    regno = cpp_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    if request.method =='POST':
        form = cpp_form(request.POST)
        if form.is_valid():
            # for i in range(len(reg)):
            #     if form.cleaned_data['regno'] == reg[i]:
            #
            #         return HttpResponse('<h1>Already attended the quiz Come Back Later</h1>')
            #     else:
                    # if dbms_score.objects.count() > 10:
                    #     object = dbms_questions.objects.oldest()
                    #     object[0].delete()
                    form.save(commit =True)
                    return render(request,'quiz/cpp_quiz.html')
        else:
            print('ERROR FORM INVALID')
    return render(request,'quiz/cpp_login.html',{'form':form})


def c_login(request):
    form = c_form()
    reg=[]
    regno = c_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    if request.method =='POST':
        form = c_form(request.POST)
        if form.is_valid():
            # for i in range(len(reg)):
            #     if form.cleaned_data['regno'] == reg[i]:
            #
            #         return HttpResponse('<h1>Already attended the quiz Come Back Later</h1>')
            #     else:
                    # if dbms_score.objects.count() > 10:
                    #     object = dbms_questions.objects.oldest()
                    #     object[0].delete()
                    form.save(commit =True)
                    return render(request,'quiz/c_quiz.html')
        else:
            print('ERROR FORM INVALID')
    return render(request,'quiz/c_login.html',{'form':form})

def dm_login(request):
    form = dm_form()
    reg=[]
    regno = dm_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    if request.method =='POST':
        form = dm_form(request.POST)
        if form.is_valid():
            # for i in range(len(reg)):
            #     if form.cleaned_data['regno'] == reg[i]:
            #
            #         return HttpResponse('<h1>Already attended the quiz Come Back Later</h1>')
            #     else:
                    # if dbms_score.objects.count() > 10:
                    #     object = dbms_questions.objects.oldest()
                    #     object[0].delete()
                    form.save(commit =True)
                    return render(request,'quiz/dm_quiz.html')
        else:
            print('ERROR FORM INVALID')
    return render(request,'quiz/dm_login.html',{'form':form})





# def dbms_form(request):
#     form = dbms_score()
#     if request.method == 'POST':
#         form = user_form(request.POST)
#         if form.is_valid():
#             form.save(commit = True)
#             return render(request,'dbms_quiz.html')
#         else:
#             print("ERROR INVALID FORM")
#     return render(request,'quiz/dbms_login.html',{'form':form})

def index(request):
    return render(request,'index.html')

# def categories(request):
#     return render(request,'categories.html')

def quiz(request):
    return render(request,'quiz/quiz.html')


def dbms_login(request):
    form = dbms_form()
    reg=[]
    regno = dbms_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    if request.method =='POST':
        form = dbms_form(request.POST)
        if form.is_valid():
            # for i in range(len(reg)):
            #     if form.cleaned_data['regno'] == reg[i]:
            #
            #         return HttpResponse('<h1>Already attended the quiz Come Back Later</h1>')
            #     else:
                    # if dbms_score.objects.count() > 10:
                    #     object = dbms_questions.objects.oldest()
                    #     object[0].delete()
                    form.save(commit =True)
                    return render(request,'quiz/dbms_quiz.html')
        else:
            print('ERROR FORM INVALID')
    return render(request,'quiz/dbms_login.html',{'form':form})



# quiz below

def dbms_quiz(request):
    p = dbms_score()
    record = dbms_score.objects.latest('id')
    print("THIS IS THE LATEST RECORD",record)
    test = request.POST.get("result"," ")
    if test != " ":
        record.Score = test
        # p = dbms_score.objects.create(Score=test)
        record.save()
    print("HEY THIS IS THE AJAX POST ",test)
    return render(request,'quiz/dbms_quiz.html')

def os_quiz(request):
    p = os_score()
    record = os_score.objects.latest('id')
    print("THIS IS THE LATEST RECORD",record)
    test = request.POST.get("result"," ")
    if test != " ":
        record.Score = test
        # p = dbms_score.objects.create(Score=test)
        record.save()
    print("HEY THIS IS THE AJAX POST ",test)
    return render(request,'quiz/os_quiz.html')

def ca_quiz(request):
    p = ca_score()
    record = ca_score.objects.latest('id')
    print("THIS IS THE LATEST RECORD",record)
    test = request.POST.get("result"," ")
    if test != " ":
        record.Score = test
        # p = dbms_score.objects.create(Score=test)
        record.save()
    print("HEY THIS IS THE AJAX POST ",test)
    return render(request,'quiz/ca_quiz.html')

def c_quiz(request):
    p = c_score()
    record = c_score.objects.latest('id')
    print("THIS IS THE LATEST RECORD",record)
    test = request.POST.get("result"," ")
    if test != " ":
        record.Score = test
        # p = dbms_score.objects.create(Score=test)
        record.save()
    print("HEY THIS IS THE AJAX POST ",test)
    return render(request,'quiz/c_quiz.html')

def cpp_quiz(request):
    p = cpp_score()
    record = cpp_score.objects.latest('id')
    print("THIS IS THE LATEST RECORD",record)
    test = request.POST.get("result"," ")
    if test != " ":
        record.Score = test
        # p = dbms_score.objects.create(Score=test)
        record.save()
    print("HEY THIS IS THE AJAX POST ",test)
    return render(request,'quiz/cpp_quiz.html')

def java_quiz(request):
    p = java_score()
    record = java_score.objects.latest('id')
    print("THIS IS THE LATEST RECORD",record)
    test = request.POST.get("result"," ")
    if test != " ":
        record.Score = test
        # p = dbms_score.objects.create(Score=test)
        record.save()
    print("HEY THIS IS THE AJAX POST ",test)
    return render(request,'quiz/java_quiz.html')

def vb_quiz(request):
    p = vb_score()
    record = vb_score.objects.latest('id')
    print("THIS IS THE LATEST RECORD",record)
    test = request.POST.get("result"," ")
    if test != " ":
        record.Score = test
        # p = dbms_score.objects.create(Score=test)
        record.save()
    print("HEY THIS IS THE AJAX POST ",test)
    return render(request,'quiz/vb_quiz.html')

def dm_quiz(request):
    p = dm_score()
    record = dm_score.objects.latest('id')
    print("THIS IS THE LATEST RECORD",record)
    test = request.POST.get("result"," ")
    if test != " ":
        record.Score = test
        # p = dbms_score.objects.create(Score=test)
        record.save()
    print("HEY THIS IS THE AJAX POST ",test)
    return render(request,'quiz/dm_quiz.html')



# REGNO and DB below

def dbms_db(request):
    quiz = dbms_questions.objects.all()
    quiz_dict = {"quizes":quiz}
    print('THIS IS THE QUIZ',quiz)
    responsedata = serializers.serialize('json',quiz,cls=LazyEncoder)
    return HttpResponse(responsedata, content_type='application/json')



def dbms_regno(request):
    reg=[]
    regno = dbms_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    print('THIS IS REG',reg)
    responsedata = json.dumps(reg)
    print('THIS IS RESPONSEDATA',responsedata)
    # print("THIS IS THE RESPONSEDATA",responsedata)
    return HttpResponse(responsedata, content_type='application/json')

def os_db(request):
    quiz = os_questions.objects.all()
    quiz_dict = {"quizes":quiz}
    print('THIS IS THE QUIZ',quiz)
    responsedata = serializers.serialize('json',quiz,cls=LazyEncoder)
    return HttpResponse(responsedata, content_type='application/json')



def os_regno(request):
    reg=[]
    regno = os_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    print('THIS IS REG',reg)
    responsedata = json.dumps(reg)
    print('THIS IS RESPONSEDATA',responsedata)
    # print("THIS IS THE RESPONSEDATA",responsedata)
    return HttpResponse(responsedata, content_type='application/json')

def ca_db(request):
    quiz = ca_questions.objects.all()
    quiz_dict = {"quizes":quiz}
    print('THIS IS THE QUIZ',quiz)
    responsedata = serializers.serialize('json',quiz,cls=LazyEncoder)
    return HttpResponse(responsedata, content_type='application/json')



def ca_regno(request):
    reg=[]
    regno = ca_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    print('THIS IS REG',reg)
    responsedata = json.dumps(reg)
    print('THIS IS RESPONSEDATA',responsedata)
    # print("THIS IS THE RESPONSEDATA",responsedata)
    return HttpResponse(responsedata, content_type='application/json')

def c_db(request):
    quiz = c_questions.objects.all()
    quiz_dict = {"quizes":quiz}
    print('THIS IS THE QUIZ',quiz)
    responsedata = serializers.serialize('json',quiz,cls=LazyEncoder)
    return HttpResponse(responsedata, content_type='application/json')



def c_regno(request):
    reg=[]
    regno = c_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    print('THIS IS REG',reg)
    responsedata = json.dumps(reg)
    print('THIS IS RESPONSEDATA',responsedata)
    # print("THIS IS THE RESPONSEDATA",responsedata)
    return HttpResponse(responsedata, content_type='application/json')

def cpp_db(request):
    quiz = cpp_questions.objects.all()
    quiz_dict = {"quizes":quiz}
    print('THIS IS THE QUIZ',quiz)
    responsedata = serializers.serialize('json',quiz,cls=LazyEncoder)
    return HttpResponse(responsedata, content_type='application/json')



def cpp_regno(request):
    reg=[]
    regno = cpp_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    print('THIS IS REG',reg)
    responsedata = json.dumps(reg)
    print('THIS IS RESPONSEDATA',responsedata)
    # print("THIS IS THE RESPONSEDATA",responsedata)
    return HttpResponse(responsedata, content_type='application/json')

def java_db(request):
    quiz = java_questions.objects.all()
    quiz_dict = {"quizes":quiz}
    print('THIS IS THE QUIZ',quiz)
    responsedata = serializers.serialize('json',quiz,cls=LazyEncoder)
    return HttpResponse(responsedata, content_type='application/json')



def java_regno(request):
    reg=[]
    regno = java_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    print('THIS IS REG',reg)
    responsedata = json.dumps(reg)
    print('THIS IS RESPONSEDATA',responsedata)
    # print("THIS IS THE RESPONSEDATA",responsedata)
    return HttpResponse(responsedata, content_type='application/json')

def vb_db(request):
    quiz = vb_questions.objects.all()
    quiz_dict = {"quizes":quiz}
    print('THIS IS THE QUIZ',quiz)
    responsedata = serializers.serialize('json',quiz,cls=LazyEncoder)
    return HttpResponse(responsedata, content_type='application/json')



def vb_regno(request):
    reg=[]
    regno = vb_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    print('THIS IS REG',reg)
    responsedata = json.dumps(reg)
    print('THIS IS RESPONSEDATA',responsedata)
    # print("THIS IS THE RESPONSEDATA",responsedata)
    return HttpResponse(responsedata, content_type='application/json')

def dm_db(request):
    quiz = dm_questions.objects.all()
    quiz_dict = {"quizes":quiz}
    print('THIS IS THE QUIZ',quiz)
    responsedata = serializers.serialize('json',quiz,cls=LazyEncoder)
    return HttpResponse(responsedata, content_type='application/json')



def dm_regno(request):
    reg=[]
    regno = dm_score.objects.values_list('regno', flat=True)
    print("THIS IS THE REGNOS",regno)
    for i in regno:
         reg.append(i)
    print('THIS IS REG',reg)
    responsedata = json.dumps(reg)
    print('THIS IS RESPONSEDATA',responsedata)
    # print("THIS IS THE RESPONSEDATA",responsedata)
    return HttpResponse(responsedata, content_type='application/json')
