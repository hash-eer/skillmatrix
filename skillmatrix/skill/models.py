from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SkillCatogary(models.Model):
    categary = models.CharField(max_length=50,null=True, blank=True)
    
    def __str__(self):
        return self.categary
    
    
class SkillLevel(models.Model):
    LEVELS = (
        ('', '----Select Skill Level ------'),
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Intern', 'Intern'),
        ('Expert', 'Expert'),
    )
    level = models.CharField(default='', choices=LEVELS, max_length=12, unique=True)
    
    def __str__(self):
        return self.level
    
    
class Skills(models.Model):
    category=models.ForeignKey(SkillCatogary, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.name
    

class Skillmatrix(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    skill=models.ForeignKey(Skills, on_delete=models.CASCADE)
    level=models.ForeignKey(SkillLevel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.skill.name
    
    

    