import base64
import json
import time

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_jwt.utils import jwt_decode_handler

from .models import userInfo_model
from .serializer import userInfo_modelSerializer, userRegisterSerializer

"""
=================================注册==========================================
"""
@api_view(["POST"])
def register(request):
    userInfo = request.data.dict()
    serializer = userInfo_modelSerializer(data=userInfo)
    if serializer.is_valid():
        # print(serializer.data)
        serializer.save()
        obj = {
                "status": 200,
                "message": "操作成功",
                "data": True,
                "timestamp": 1692770915226
        }
        return Response(data=obj, status=status.HTTP_200_OK)
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
    if userInfo_model.objects.filter(username=username).exists():
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
    if userInfo_model.objects.filter(tel=phone_num).exists():
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


"""
=================================登录==============================================
"""
@api_view(["POST"])
def user_Login(request):
    username = request.data.dict()['username']
    password = request.data.dict()['password']
    if userInfo_model.objects.filter(username=username, password=password).exists():
        user = userInfo_model.objects.get(username=username, password=password)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        print(access_token)
        json_obj = {
            "status": 200,
            "message": "操作成功",
            "data": "{}".format(access_token),
            "timestamp": int(time.time())
        }
        return Response(data=json_obj, status=status.HTTP_200_OK)
    else:
        json_obj = {
              "status": 999,
              "message": "用户名或密码错误",
              "data": None,
              "timestamp": 1692624990691
        }
        return Response(data=json_obj, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(["POST", "OPTIONS"])
def user_Logout(request):
    print(request.data)
    print(request.body)
    return Response(status=status.HTTP_200_OK)

@csrf_exempt
@api_view(["GET", "OPTIONS"])
def getCurrentUser(request):
    if request.method == 'GET':
        jwt = request.query_params.get("dd-authorization")
        # token_user = jwt_decode_handler(jwt)
        # user = token_user['username']
        print(jwt)
        return Response(status=status.HTTP_200_OK)
    if request.method == 'OPTIONS':
        jwt = request.query_params.get("dd-authorization")
        token_user = jwt_decode_handler(jwt)
        user = token_user['username']
        print(token_user)
        return Response(status=status.HTTP_200_OK)