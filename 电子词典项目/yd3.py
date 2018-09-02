#!/usr/bin/env python3
#coding=utf-8

'''
name:yang
MODULES:python3.5 mysql pymysql
This is a dict project for AID
'''
from socket import *
import sys
import traceback
import getpass

#主控制流程函数
def main():
    if len(sys.argv)<3:
        print('argv is error')
        return
    host=sys.argv[1]
    port=int(sys.argv[2])
    s=socket()
    try:
        s.connect((host,port))
    except Exception:
        traceback.print_exc()
        return
    while True:
        print('进入一级界面,请选择')
        print('''
            ==========welcone===========
            ---1.登录  2.注册  3.退出---
            ============================
            ''')
        try:
            cmd=int(input('请输入选项>>>'))
        except Exception:
            print('输入有误!')
            continue
        if cmd not in [1,2,3]:
            print('没有该选项!!')
            continue
        elif cmd==1:
            if denglu(s)==0:
                print('登录成功!!')
                login(s)
        elif cmd==2:
            if zhuce(s) == 0:
                print('注册成功!,可以登录')
            else:
                print('注册失败!')
        elif cmd==3:
            s.send(b'Sign out')
            sys.exit('谢谢使用')

def zhuce(s):
    while True:
        name=input('用户名:')
        passwd=getpass.getpass('密码:')
        passwd1=getpass.getpass('确认密码:')
        if (' 'in name)or(' 'in passwd):
            print("用户名或密码不能有空格")
            continue
        if passwd != passwd1:
            print('两次密码不一致')
            continue
        msg='R {} {}'.format(name,passwd)
        s.send(msg.encode())
        data=s.recv(128).decode()
        if data =='OK':
            return 0
        elif data=='exists':
            return 1
        else:
            return 1

def denglu(s):
    name=input('用户名:')
    passwd=getpass.getpass()
    msg='L {} {}'.format(name,passwd)
    s.send(msg.encode())
    data=s.recv(128).decode()
    if data == 'OK':
        return 0
    else:
        print("用户名或密码不正确!!!")
        return 1

#登录后进入二级界面
def login(s):
    while True:
        print('''
            **************************************************
            **0.英汉查词**1.英语查词**2.查看历史查询**3.退出**
            **************************************************
            ''')
        x=input('请选择>>>')
        if x=='0':
            s.send('W'.encode())
            yhci(s)
        elif x=='1':
            s.send('H'.encode())
            chaci(s)
        elif x=='2':
            s.send('Q'.encode())
            chkan(s)
        elif x=='3':
            break

def yhci(s):
    print('----------进入英汉查词----------')
    while True:
        x=input('请输入单词(输入##退出)>>')
        if x=='##':
            s.send('##'.encode())
            break
        else:
            s.send(x.encode())
            data=s.recv(128).decode()
            if data=='No use of this word':
                print('No use of this word')
                continue
            else:
                print(data)


def chaci(s):
    print('----------进入英语查词----------')
    while True:
        x=input('请输入单词(输入##退出)>>')
        if x=='##':
            s.send('##'.encode())
            break
        else:
            s.send(x.encode())
            data=s.recv(128).decode()
            if data=='No use of this word':
                print('No use of this word')
                continue
            else:
                print(data)

def chkan(s):
    while True:
        data = s.recv(128).decode()
        print(data)
        if data == 'OK':
            while True:
                data = s.recv(1024).decode()
                if data=='over':
                    break
                print(data)
        else:
            print("没有历史记录")
        break


if __name__ == '__main__':
    main()