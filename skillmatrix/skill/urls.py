from django.urls import path
from skill import views
urlpatterns = [
    path('add_skill/',views.add_skill_matrix, name='add_skill_matrix'),
    # pat/h('view/<int:id>/',views.skill_view,name="view"),
    path('',views.listskill,name="list"),
    


    
]