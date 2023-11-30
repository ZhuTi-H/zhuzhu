import base64
import json
import time

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import viewsets

from .models import userInfo_model
from .serializer import userInfo_modelSerializer, userRegisterSerializer

@api_view(["GET", "POST"])
def createUser(request):
    name = request.query_params.get('name', None)
    print(request.data)
    # user_obj = userInfo_model.objects.all()
    # name = request.POST.get("name")
    print(name)
    serializer = userInfo_modelSerializer(data=request.data)
    # print(serializer)
    # print(user_obj)
    if serializer.is_valid():
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def register(request):
    data = json.loads(request.body)
    print(data)
    serializer = userRegisterSerializer(data=request.body)
    if serializer.is_valid():
        print(serializer.data)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def checkCode(request):
    serializer = userInfo_modelSerializer(data=request.data)

    if serializer.is_valid():
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def isExist_userName(request):
    username = request.query_params.get('username', None)
    print(username)
    if userInfo_model.objects.filter(name=username).exists():
        json_obj = {
            "status": 200,
            "message": '用户名已存在',
            "data": True,
            "timestamp": int(time.time())
        }
        return Response(data=json_obj, status=status.HTTP_200_OK)
    else:
        json_obj = {
            "status": 200,
            "message": '允许注册',
            "data": False,
            "timestamp": int(time.time())
        }
        return Response(data=json_obj, status=status.HTTP_200_OK)

@api_view(["GET", "POST"])
def isExist_Tel(request):
    phone_num = request.query_params.get("tel", None)
    print(phone_num)
    if userInfo_model.objects.filter(phone=phone_num).exists():
        json_obj = {
            "status": 200,
            "message": '电话已存在',
            "data": True,
            "timestamp": int(time.time())
        }
        return Response(data=json_obj, status=status.HTTP_200_OK)
    else:
        json_obj = {
            "status": 200,
            "message": '电话允许注册',
            "data": False,
            "timestamp": int(time.time())
        }
        return Response(data=json_obj, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def checkTel_checkCode(request):
    phone_num = request.query_params.get("tel", None)
    code = request.query_params.get("telCheckCode", None)
    # 简单逻辑测试，后续更改
    if code == '123456':
        json_obj = {
            "status": 200,
            "message": '验证成功',
            "data": True,
            "timestamp": int(time.time())
        }
        return Response(data=json_obj, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def check_checkCode(request):
    checkCode = request.query_params.get("checkCode", None)
    # 简单逻辑测试，后续更改
    if checkCode == 'ABCD':
        json_obj = {
            "status": 200,
            "message": '验证成功',
            "data": True,
            "timestamp": int(time.time())
        }
        return Response(data=json_obj, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)