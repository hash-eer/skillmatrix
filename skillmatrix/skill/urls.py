from django.urls import path
from skill import views
from skill.views import *
urlpatterns = [
    path('list',views.skill_list,name="list"),
]