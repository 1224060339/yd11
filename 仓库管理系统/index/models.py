from django.db import models

# Create your models here.

class Users(models.Model):
    # 电话号码 - CharField()
    uphone = models.CharField(max_length=11)
    # 密码 - CharField()
    upwd = models.CharField(max_length=30)
    # 电子邮件 - EmailField()
    uemail = models.EmailField()
    # 用户名 - CharField()
    uname = models.CharField(max_length=20)
    # 启用/禁用 - BooleanField(),默认值为True
    isActive = models.BooleanField(default=True)
class SHP(models.Model):
    shpmc = models.CharField(max_length=50)
    shpshl = models.CharField(max_length=6)
    shpjg = models.CharField(max_length=6)
