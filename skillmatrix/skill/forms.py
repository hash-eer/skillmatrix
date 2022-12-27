from django.forms import  ModelForm, TextInput, Select,ChoiceField,HiddenInput, Form
from skill.models import Skillmatrix,Skills,SkillCatogary,SkillLevel
from django import forms



class TechForm(Form):

    t_skill = forms.ModelChoiceField(queryset=Skills.objects.filter(category__category='technology'), widget=Select(
                         attrs={'class': "custom-select col-md-4"}), required=False, label='Skill')
    t_level = forms.ModelChoiceField(required=False, queryset=SkillLevel.objects.all(), widget=Select(
                         attrs={'class': "custom-select col-md-4"}), label='Level')
        


  
class FrameworkForm(Form):
    f_skill = forms.ModelChoiceField(queryset=Skills.objects.filter(category__category='framework'), widget=Select(
                         attrs={'class': "custom-select col-md-4"}),required=False, label='Skill')
    f_level = forms.ModelChoiceField(required=False, queryset=SkillLevel.objects.all(), widget=Select(
                         attrs={'class': "custom-select col-md-4"}), label='Level')
 
 
class DatabaseForm(Form):
    
    d_skill = forms.ModelChoiceField(queryset=Skills.objects.filter(category__category='database'), widget=Select(
                         attrs={'class': "custom-select col-md-4"}), required=False, label='Skill')
    d_level = forms.ModelChoiceField(required=False, queryset=SkillLevel.objects.all(), widget=Select(
                         attrs={'class': "custom-select col-md-4"}), label='Level')
    
    
class OSForm(Form):
   
    o_skill = forms.ModelChoiceField(queryset=Skills.objects.filter(category__category='operating system'), widget=Select(
                         attrs={'class': "custom-select col-md-4"}), required=False, label='Skill')
    o_level = forms.ModelChoiceField(required=False, queryset=SkillLevel.objects.all(), widget=Select(
                         attrs={'class': "custom-select col-md-4"}), label='Level')
    
    
    
class WebApiForm(Form):
   
    w_skill = forms.ModelChoiceField(queryset=Skills.objects.filter(category__category='web-api'), widget=Select(
                         attrs={'class': "custom-select col-md-4"}), required=False,label='Skill')
    w_level = forms.ModelChoiceField(required=False, queryset=SkillLevel.objects.all(), widget=Select(
                         attrs={'class': "custom-select col-md-4"}), label='Level')
    
   