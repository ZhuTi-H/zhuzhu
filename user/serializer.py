# -*- coding: utf-8 -*-
# 作者: 猪蹄涵
# 网站: zhuzhuit.cn

from rest_framework.serializers import Serializer
from rest_framework import serializers

from .models import userInfo_model


class userInfo_modelSerializer(serializers.ModelSerializer):

    class Meta:
        model = userInfo_model
        fields = '__all__'



class userRegisterSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(label='用户名')
    password = serializers.CharField(label='密码')
    tel = serializers.CharField(label='联系方式')
    emergencyTel = serializers.CharField(label='紧急联系方式')
    email = serializers.CharField(label='邮箱')
    cid = serializers.CharField(label='ID')

    class Meta:
        model = userInfo_model
        fields = ('userName', 'password', 'tel', 'emergencyTel', 'email', 'cid')


