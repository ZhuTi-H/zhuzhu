# -*- coding: utf-8 -*-
# 作者: 猪蹄涵
# 网站: zhuzhuit.cn

from django.urls import path
from .views import (register, checkCode,isExist_userName,
                    isExist_Tel, checkTel_checkCode,
                    check_checkCode, user_Login, user_Logout,
                    getCurrentUser)


urlpatterns = [
    path('register/', register),
    path('checkCode/', checkCode),
    path('user/login', user_Login),
    path('user/logout', user_Logout),
    path('user/getCurrentUser', getCurrentUser),
    path('user/permitApi/isExistUsername/', isExist_userName),
    path('user/permitApi/isExistTel/', isExist_Tel),
    path('checkTelCheckCode/', checkTel_checkCode),
    path('checkCheckCode/', check_checkCode),
]