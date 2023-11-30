# -*- coding: utf-8 -*-
# 作者: 猪蹄涵
# 网站: zhuzhuit.cn
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import viewsets

from .models import userInfo_model
from .serializer import userInfo_modelSerializer