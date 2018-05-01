# -*- coding: utf-8 -*-
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime as dt
from django.contrib.auth.models import User
import cv2
import os
import sys
import traceback
import json
import urllib

def login(req):
    return render(req, 'login.html')

def management(req):
    return render(req, 'management.html', login_data) #urlsのsampleを定義

def menu(req):
    global login_data
    if req.method == 'POST':
        user_id = req.POST['id']
        user_password = req.POST['password']
#        user_db = USER.objects.all().order_by('id')

        login_data = {
             'datetime':dt.now().strftime("%Y/%m/%d %H:%M"),
             'user_id': user_id,
             'user_password': user_password,
        }
        return render(req, 'menu.html', login_data)
    else:
        return render(req, 'menu.html', login_data)

def calculate(req):
    return render(req, 'calculator.html', login_data)

def calculate2(req):
    return render(req, 'calculator2.html', login_data)

def video(req):
    return render(req, 'video.html', login_data)

def support(req):
    return render(req, 'helpQA.html', login_data)

def qrcode(req):
    return render(req, 'qrcode.html', login_data)



# Create your views here.
