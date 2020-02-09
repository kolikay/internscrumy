
from django.urls import path, include
from kolikay1989scrumy import views


urlpatterns = [
    path('index', views.index, name ="index"),
    path('movegoal/<int:goal_id>', views.move_goal, name="movegoal"),
    #path('movegoal', views.move_goal, name="movegoal"),
    path('addgoal', views.add_goal, name="addgoal"),
    path('home', views.home, name="home"), 
    path('accounts/', include('django.contrib.auth.urls'), name = "login"),
  
  
]