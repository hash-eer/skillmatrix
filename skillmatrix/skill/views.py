from django.shortcuts import render,redirect
from skill.models import Skillmatrix, Skills,SkillLevel,SkillCatogary
from django.contrib.auth.models import User
from django.http import HttpResponse
from skill.forms import TechForm,FrameworkForm,DatabaseForm,OSForm,WebApiForm
from django.forms import formset_factory

# Create your views here.
def home(request):
    return HttpResponse("hey hello")


def listskill(request):
    
    s = Skills.objects.all()
    l=SkillLevel.objects.all()
    
    technology=Skillmatrix.objects.filter(skill__category__category="technology")
    framework=Skillmatrix.objects.filter(skill__category__category="framework")
    database=Skillmatrix.objects.filter(skill__category__category="database")
    os=Skillmatrix.objects.filter(skill__category__category="operating system")
    webapi=Skillmatrix.objects.filter(skill__category__category="web api")
    
    
   
    if request.GET.get('level') and  request.GET.get('skill'):
        sk = request.GET.get('skill')
        lev= request.GET.get('level')
        print(lev)
    
       
        
        skills = Skillmatrix.objects.filter(skill=sk,level=lev).order_by('user__username').distinct('user__username')
        data = {'skill':skills, 's':s,'l':l,'technology':technology,'framework':framework,'database':database,'os':os,'webapi':webapi}
        return render(request, 'search.html', data)
    
    if request.GET.get('skill'):
        q = request.GET.get('skill')
        print(q)
     
        skills = Skillmatrix.objects.filter(skill=q).order_by('user__username').distinct('user__username')
        data = {'skill':skills, 's':s,'l':l,'technology':technology,'framework':framework,'database':database,'os':os,'webapi':webapi}
        return render(request, 'search.html', data)
    
    if request.GET.get('level') and request.GET.get:
        q = request.GET.get('level')
        print(q)
     
        skills = Skillmatrix.objects.filter(level=q).order_by('user__username').distinct('user__username')
        data = {'skill':skills, 's':s,'l':l,'technology':technology,'framework':framework,'database':database,'os':os,'webapi':webapi}
        return render(request, 'search.html', data)
    
    
        
    
    skills = Skillmatrix.objects.all().order_by('user__username').distinct('user__username')
    data = {'skill':skills, 's':s,'l':l,'technology':technology,'framework':framework,'database':database,'os':os,'webapi':webapi}
    
    return render(request, 'list_skill.html', data)





def add_skill_matrix(request):
    tech_form_set = formset_factory(TechForm)
    tech_form = tech_form_set()
    
    framework_form_set = formset_factory(FrameworkForm, extra=1)
    framework_form = framework_form_set()
    
    db_form_set = formset_factory(DatabaseForm,extra=1)
    db_form = db_form_set()
    
    os_form_set = formset_factory(OSForm,extra=1)
    os_form = os_form_set()
    
    web_form_set = formset_factory(WebApiForm,extra=1)
    web_form = web_form_set()
    # os_form = OSForm(request.POST or None)
    # webapi_form = WebApiForm(request.POST or None)
    user = request.user
    print(tech_form)
 
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        tech_form = tech_form_set(request.POST or None)
        framework_form = framework_form_set(request.POST or None)
        db_form = db_form_set(request.POST or None)
        os_form = os_form_set(request.POST or None)
        web_form = web_form_set(request.POST or None)
        
        print(user)
        if tech_form.is_valid() and framework_form.is_valid() and db_form.is_valid() and os_form.is_valid() and web_form.is_valid():
        # or framework_form.is_valid() and db_form.is_valid() and os_form.is_valid() and webapi_form.is_valid():
        # and framework_form.is_valid() and db_form.is_valid() and os_form.is_valid() and webapi_form.is_valid():
            for form in tech_form:
                t_skill = form.cleaned_data.get('t_skill')
                t_level = form.cleaned_data.get('t_level')
                t = Skillmatrix(skill=t_skill, level=t_level, user=user)
                t.save() 
                
            for form in framework_form:
                f_skill = form.cleaned_data.get('f_skill')
                f_level = form.cleaned_data.get('f_level')
                f = Skillmatrix(skill=f_skill, level=f_level, user=user)
                f.save() 
            
            for form in db_form:
                d_skill = form.cleaned_data.get('d_skill')
                d_level = form.cleaned_data.get('d_level')
                d = Skillmatrix(skill=d_skill, level=d_level, user=user)
                d.save() 
                
            for form in os_form:
                
                o_skill = form.cleaned_data.get('o_skill')
                o_level = form.cleaned_data.get('o_level')
                o = Skillmatrix(skill=o_skill, level=o_level, user=user)
                print(o_skill)
                o.save() 
                
            for form in web_form:
                w_skill = form.cleaned_data.get('w_skill')
                w_level = form.cleaned_data.get('w_level')
                w = Skillmatrix(skill=w_skill, level=w_level, user=user)
                w.save() 
                
            else:
                for form in tech_form:
                    print(tech_form.errors)
        return redirect('list')
    
    forms = {'tech_form':tech_form,'framework_form':framework_form,'db_form':db_form,'os_form':os_form,'web_form':web_form}
           
    return render(request, 'add_skill.html', forms)




        
        
