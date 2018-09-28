from django import forms
from django.contrib.auth.models import User
from quiz.models import *


class dbms_form(forms.ModelForm):
    class Meta():
        model = dbms_score
        fields = ('name','regno','year')


class c_form(forms.ModelForm):
    class Meta():
        model = c_score
        fields = ('name','regno','year')

class os_form(forms.ModelForm):
    class Meta():
        model = os_score
        fields = ('name','regno','year')

class vb_form(forms.ModelForm):
    class Meta():
        model = vb_score
        fields = ('name','regno','year')

class dm_form(forms.ModelForm):
    class Meta():
        model = dm_score
        fields = ('name','regno','year')

class cpp_form(forms.ModelForm):
    class Meta():
        model = cpp_score
        fields = ('name','regno','year')

class java_form(forms.ModelForm):
    class Meta():
        model = java_score
        fields = ('name','regno','year')

class ca_form(forms.ModelForm):
    class Meta():
        model = ca_score
        fields = ('name','regno','year')
