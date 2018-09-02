from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
import json
from django.core import serializers

# Create your views here.
def login_views(request):
    if request.method == 'GET':
        return render(request,'登录.html')
    else:
        upwd=request.POST['upwd']
        uname=request.POST['uname']
        uList = Users.objects.filter(uname=uname, upwd=upwd)
        if uList:
            resp = HttpResponse('欢迎:' + uname)
            if 'isSaved' in request.POST:
                # 分两次将　uphone 和　id 存进　cookie
                expires = 60 * 60 * 24 * 365
                resp.set_cookie('id', uList[0].id, expires)
                resp.set_cookie('uname', uname, expires)
                return render(request,'管理.html',locals())
            else:
                return render(request,'管理.html',locals())
        else:
            a='用户名或密码不正确！！！'
            return render(request,'登录.html',locals())

def register_views(request):
    if request.method == 'GET':
        return render(request,'注册.html')
    else:
        uname=request.POST['uname']
        upwd=request.POST['upwd']
        upwd1=request.POST['upwd1']
        uphone=request.POST['uphone']
        uemail=request.POST['uemail']
        uList = Users.objects.filter(uname=uname)
        uList1 = Users.objects.filter(uphone=uphone)
        uList2 = Users.objects.filter(uemail=uemail)
        if uList:
            a='用户名已存在!'
            return render(request,'注册.html',locals())
        elif uList1:
            b='电话号码已注册!'
            return render(request,'注册.html',locals())
        elif uList2:
            c='电子邮箱已注册!'
            return render(request,'注册.html',locals())
        else:
            dic = {
            'uphone': uphone,
            'upwd': upwd,
            'uname': uname,
            'uemail': uemail,
            }
        Users(**dic).save()
        return render(request,'注册成功.html')

def login1_views(request):
    if request.method == 'GET':
        return render(request,'www.html')
    else:
        i=0
        ushpmc=[]
        ushpshl=[]
        ushpjg=[]
        while i>=0:
            if i==0:
                ushpmc.append(request.POST['ushpmc'])
                ushpshl.append(request.POST['ushpshl'])
                ushpjg.append(request.POST['ushpjg'])
            else:
                try:
                    ushpmc.append(request.POST['ushpmc'+str(i)])
                    ushpshl.append(request.POST['ushpshl'+str(i)])
                    ushpjg.append(request.POST['ushpjg'+str(i)])
                except Exception:
                    break
            i+=1
        for x in ushpmc:
            if x=='':
                a='请输入第一条数据!!'
                return render(request,'www.html',locals())
            uList = SHP.objects.filter(shpmc=x)
            if uList:
                a=str(x)+'已存在,请重新添加！'
                return render(request,'www.html',locals())
        for i in range(len(ushpmc)):
            dic={
                'shpmc':str(ushpmc[i]),
                'shpshl':str(ushpshl[i]),
                'shpjg':str(ushpjg[i])
            }
            SHP(**dic).save()
        return render(request,'sss.html')

def login2_views(request):
    shps=SHP.objects.all()
    return render(request,'ssy.html',locals())

def login3_views(request):
    if request.method == 'GET':
        return render(request,'xiugai.html')
    else:
        i=0
        ushpmc=[]
        ushpshl=[]
        ushpjg=[]
        while i>=0:
            if i==0:
                ushpmc.append(request.POST['ushpmc'])
                ushpshl.append(request.POST['ushpshl'])
                ushpjg.append(request.POST['ushpjg'])
            else:
                try:
                    ushpmc.append(request.POST['ushpmc'+str(i)])
                    ushpshl.append(request.POST['ushpshl'+str(i)])
                    ushpjg.append(request.POST['ushpjg'+str(i)])
                except Exception:
                    break
            i+=1
        x=0
        for shpmc in ushpmc:
            List=SHP.objects.filter(shpmc=shpmc)
            if shpmc=='':
                a='请输入第一条要修改的商品!'
                return render(request,'xiugai.html',locals())
            elif List:
                List.update(shpshl=ushpshl[x],shpjg=ushpjg[x])
            else:
                a=shpmc+'不存在请先添加！'
                return render(request,'xiugai.html',locals())
            x+=1
        return render(request,'wwy.html')