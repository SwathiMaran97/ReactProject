
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from menu.models import *
from django.http import HttpResponse




def create(request):
    print('yyrewuruu')
    issue_category = menu.objects.all()
    
    return issue_category
npm install -g create-react-app
npx create-react-app myfirstreact
npm start