from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import ScrumyGoals, GoalStatus
import random
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login, authenticate
from kolikay1989scrumy.forms import (SignUpForm,DeveloprCreateGoalForm, QACreateGoalForm,OwnerChangeGoalForm,
                                        ChangeGoalForm,CreateGoalForm, QAChangeGoalForm1,OwnerCreateGoalForm,
                                        QAChangeGoalForm, AdminChangeGoalForm,DeveloperChangeGoalForm)
from django.contrib.auth.models import Group

def home(request):
    users = User.objects.all()


    def get_by_status(status_name):
        goals = GoalStatus.objects.get(status_name=status_name)
        status_goals = goals.scrumygoals_set.all()
        return status_goals
    daily_goals = get_by_status("Daily Goal")
    weekly_goals = get_by_status("Weekly Goal")
    verify_goals = get_by_status("Verify Goal")
    done_goals = get_by_status("Done Goal")
    dictionary = {
    'users': users,
    'weekly_goals': weekly_goals,
    'daily_goals': daily_goals,
    'verify_goals': verify_goals,
    'done_goals': done_goals,}
    return render(request, 'kolikay1989scrumy/home.html', dictionary)
  



def index(request, *args, **kwargs):
   
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.groups.add(Group.objects.get(name='Developer'))
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/kolikay1989scrumy/home')
        else:
            return HttpResponse("Invalid credentials provided: Username or Email already exist")
    else:
        form = SignUpForm()
    return render (request, 'kolikay1989scrumy/index.html', {'form' : form})





# def move_goal(request, goal_id):
#     qs = User.objects.filter(groups__name__in=['Developer'])
#     obj= get_object_or_404(ScrumyGoals, goal_id=goal_id)
#     form = MoveGoalForm(request.POST or None, instance = obj)
#     goal = GoalStatus.objects.get(status_name="Done Goal")
#     #print(goal.status_name)
#     context= {'form': form}
#     if form.is_valid():
#         obj = form.save(commit= False)
#         #Making sure Developer group can only move goals to other group aside done goal
#         if request.user in qs:
#             print(obj.goal_status == "Done Goal")
#             #print(obj.goal_status)
#             obj.save()
#             return redirect("/kolikay1989scrumy/home")
#         return HttpResponse("You are not authorized to move that goal")
            
#     return render(request,'kolikay1989scrumy/movegoal.html' , context)



def add_goal(request, *args, **kwargs):
    dev = User.objects.filter(groups__name__in=['Developer'])
    qa = User.objects.filter(groups__name__in=['Quality Assurance'])
    admin = User.objects.filter(groups__name__in=['Admin'])
    own = User.objects.filter(groups__name__in=['Owner'])
    if request.user in dev:
        form = DeveloprCreateGoalForm()
        dictionary = {'form' : form}
        if request.method =='POST':
            form = DeveloprCreateGoalForm(request.POST)
            if form.is_valid():
                add_goal = ScrumyGoals()
                add_goal = form.save(commit = False)
                add_goal.goal_id = random.randint(1000, 9999)
                add_goal.goal_status = GoalStatus.objects.get(status_name="Weekly Goal")
                add_goal.save()
                return redirect  ("/kolikay1989scrumy/home")       
            return HttpResponse("Invalid credentials provided, please fill out all fields")
        else:
            form = DeveloprCreateGoalForm()
            return render (request, 'kolikay1989scrumy/addgoal.html', dictionary)
    
        
    elif request.user in qa:
        form = QACreateGoalForm()
        dictionary = {'form' : form}
        if request.method =='POST':
            form = QACreateGoalForm(request.POST)
            if form.is_valid():
                add_goal = ScrumyGoals()
                add_goal = form.save(commit = False)
                add_goal.goal_id = random.randint(1000, 9999)
                add_goal.goal_status = GoalStatus.objects.get(status_name="Weekly Goal")
                add_goal.save()
                add_goal.save()
                return redirect  ("/kolikay1989scrumy/home")       
            return HttpResponse("Invalid credentials provided, please fill out all fields")
        else:
            form = QACreateGoalForm()
    
        return render (request, 'kolikay1989scrumy/addgoal.html', dictionary)
    elif request.user in admin:
        form = CreateGoalForm()
        dictionary = {'form' : form}
        if request.method =='POST':
            form = CreateGoalForm(request.POST)
            if form.is_valid():
                add_goal = ScrumyGoals()
                add_goal = form.save(commit = False)
                add_goal.goal_id = random.randint(1000, 9999)
                add_goal.save()
                return redirect  ("/kolikay1989scrumy/home")       
            return HttpResponse("Invalid credentials provided, please fill out all fields")
        else:
            form = CreateGoalForm()
    
        return render (request, 'kolikay1989scrumy/addgoal.html', dictionary)
    elif request.user in own:
        form = CreateGoalForm()
        dictionary = {'form' : form}
        if request.method =='POST':
            form = CreateGoalForm(request.POST)
            if form.is_valid():
                add_goal = ScrumyGoals()
                add_goal = form.save(commit = False)
                add_goal.goal_id = random.randint(1000, 9999)
                add_goal.save()
                return redirect  ("/kolikay1989scrumy/home")       
            return HttpResponse("Invalid credentials provided, please fill out all fields")
        else:
            form = CreateGoalForm()
    
        return render (request, 'kolikay1989scrumy/addgoal.html', dictionary)




def move_goal(request, goal_id):
    current_user = request.user
    usr_grp = request.user.groups.all()[0]
    print(usr_grp)
    goals = get_object_or_404(ScrumyGoals, goal_id=goal_id)
    if usr_grp == Group.objects.get(name='Developer') and current_user == goals.user:
        if request.method == 'POST':
            form = DeveloperChangeGoalForm(request.POST)
            if form.is_valid():
                selected_status = form.save(commit=False)
                selected = GoalStatus.objects.all()
                selected = form.cleaned_data['goal_status']
                choice = GoalStatus.objects.get(id=int(selected))
                goals.goal_status = choice
                goals.save()
                return redirect("/kolikay1989scrumy/home")
        else:
            form = DeveloperChangeGoalForm()
        

    elif usr_grp == Group.objects.get(name='Quality Assurance') and current_user == goals.user:
        if request.method == 'POST':
            form = QAChangeGoalForm(request.POST)
            if form.is_valid():
                selected_status = form.save(commit=False)
                selected = form.cleaned_data['goal_status']
                # get_status = selected_status.goal_status
                choice = GoalStatus.objects.get(id=int(selected))
                goals.goal_status = choice
                goals.save()
                return redirect ("/kolikay1989scrumy/home")
        else:
            form = QAChangeGoalForm()
    elif usr_grp == Group.objects.get(name='Quality Assurance') and current_user != goals.user:
        print(current_user != goals.user)
        if request.method == 'POST':
            form = QAChangeGoalForm1(request.POST)
            if form.is_valid():
                selected_status = form.save(commit=False)
                selected = form.cleaned_data['goal_status']
                choice = GoalStatus.objects.get(id=int(selected))
                goals.goal_status = choice
                goals.save()
                return redirect ("/kolikay1989scrumy/home")
        form = QAChangeGoalForm1()
    elif usr_grp == Group.objects.get(name='Owner') and current_user == goals.user:
        if request.method == 'POST':
            form = OwnerChangeGoalForm(request.POST)
            if form.is_valid():
                selected_status = form.save(commit=False)
                selected = form.cleaned_data['goal_status']
                choice = GoalStatus.objects.get(id=int(selected))
                goals.goal_status = choice
                goals.save()
                return redirect ("/kolikay1989scrumy/home")
        form = OwnerChangeGoalForm()

    elif usr_grp == Group.objects.get(name='Admin'):
        if request.method == 'POST':
            form = AdminChangeGoalForm(request.POST)
            if form.is_valid():
                selected_status = form.save(commit=False)
                selected = form.cleaned_data['goal_status']
                choice = GoalStatus.objects.get(id=int(selected))
                goals.goal_status = choice
                goals.save()
                return redirect ("/kolikay1989scrumy/home")
    else:
        return HttpResponse('You  are not autorised to move this goal')
    form = AdminChangeGoalForm()
    return render(request, 'kolikay1989scrumy/movegoal.html',
                  {'form': form, 'goals': goals, 'current_user': current_user}  )
    
    
    
  

   







