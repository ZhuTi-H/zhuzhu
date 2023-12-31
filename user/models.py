from django.db import models

# Create your models here.

class userInfo_model(models.Model):
    id = models.AutoField(verbose_name='序号', primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=100)
    password = models.CharField(verbose_name='密码', max_length=100)
    tel = models.CharField(verbose_name='联系方式', max_length=11)
    emergencyTel = models.CharField(verbose_name='紧急联系方式', max_length=11)
    email = models.CharField(verbose_name='邮箱', max_length=100)
    sex = models.SmallIntegerField(verbose_name='性别', null=True)
    age = models.SmallIntegerField(verbose_name='年龄', null=True)
    create_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    avatar = models.ImageField(upload_to='userAvatar', default='default.jpg')
    class Meta:
        db_table = 'userInfo'   # 数据库别名

        verbose_name = '用户信息'    # 管理界面别名