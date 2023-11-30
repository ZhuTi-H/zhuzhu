# -*- coding: utf-8 -*-
# 作者: 猪蹄涵
# 网站: zhuzhuit.cn

from django.urls import path
from .views import (createUser, register, checkCode,
                    isExist_userName, isExist_Tel, checkTel_checkCode,
                    check_checkCode)

urlpatterns = [
    path("createUser/", createUser),
    path('register/', register),
    path('checkCode/', checkCode),
    path('user/permitApi/isExistUsername', isExist_userName),
    path('user/permitApi/isExistTel', isExist_Tel),
    path('checkTelCheckCode/', checkTel_checkCode),
    path('checkCheckCode', check_checkCode)
]
