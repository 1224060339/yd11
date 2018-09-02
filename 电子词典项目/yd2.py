#!/usr/bin/env python3
#coding=utf-8

'''
name:yang
MODULES:python3.5 mysql pymysql
This is a dict project for AID
'''

import traceback
from socket import *
import os
import signal
import time
import sys
import pymysql
from imp import reload
reload(pymysql)

HOST='127.0.0.1'
PORT=6666
ADDR=(HOST,PORT)
DICT_TEXT='./dict.txt'  #文本路径

#主控制流程
def main():
    #数据库连接
    db=pymysql.connect('localhost','root','123456','yd',charset='utf8')
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    #忽略子进程退出
    #signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            c,addr=s.accept()
            print('connect from',addr)
        except KeyboardInterrupt:
            sys.exit('服务器退出')
        except Exception:
            continue

        pid=os.fork()

        if pid == 0:
            s.close()
            do_child(c,db,addr)
        else:
            c.close()
            continue

def do_child(c,db,addr):
    #循环接收客户端请求
    while True:
        data=c.recv(128).decode()
        if data=='Sign out':
            print(addr,'已退出')
            break
        elif data[0]=='R':
            zhuce(c,db,data)
        elif data[0]=='L':
            name=denglu(c,db,data)
        elif data[0]=='E':
            c.clos()
            sys.exit(0)
        elif data[0]=='W':
            hycx(c,db,name)
        elif data[0]=='H':
            chaxun(c,db,name)
        elif data[0]=='Q':
            chakan(c,db,name)

def denglu(c,db,data):
    print('登录操作')
    l=data.split(' ')
    name=l[1]
    passwd=l[2]
    cursor=db.cursor()
    sql="select * from user where name='%s' and passwd='%s'"%(name,passwd)
    cursor.execute(sql)
    db.commit()
    r = cursor.fetchone()
    if r == None:
        c.send(b'FALL')
    else:
        c.send(b'OK')
        return name

def zhuce(c,db,data):
    print('>>>>>进入注册操作>>>>>')
    l=data.split(' ')
    name=l[1]
    passwd=l[2]
    cursor=db.cursor()
    #判断name是否存在
    sql='select name from user where name="%s";'%name
    cursor.execute(sql)
    db.commit()
    r = cursor.fetchone()
    if r != None:
        c.send(b'exists')
        return
    try:
        sql='insert into user(name,passwd) values("%s","%s");'%(name,passwd)
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        c.send(b'FALL')
        db.rollback()
        return
    else:
        print('注册成功')


def hycx(c,db,name):
    print('进入英汉查词界面')
    while True:
        data=c.recv(128).decode()
        l=data
        if l=='##':
            break
        cursor=db.cursor()
        #查找单词l[1]
        sql="select word,interpret from words1 where word='%s' or interpret='%s';"%(l,l)
        try:
            cursor.execute(sql)
            db.commit()
            r=cursor.fetchone()
        except:
            s='查询错误!'
            c.send(s.encode())
            continue
        if r==None:
            b='没有该单词!'
            c.send(b.encode())
            continue
        else:
            print(r)
            msg = "{} :　{}".format(r[0],r[1])
            c.send(msg.encode())
        def charu(name,l):
            tm = time.ctime()
            sql = "insert into hist (name,word,time) values ('%s','%s','%s')"%(name,l,tm)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
                print('插入历史记录失败!!!')
                return
        charu(name,l)


def chaxun(c,db,name):
    print('进入英语查词界面')
    while True:
        data=c.recv(128).decode()
        l=data
        if l=='##':
            break
        cursor=db.cursor()
        #查找单词l[1]
        sql="select word,interpret from words where word='%s';"%l
        try:
            cursor.execute(sql)
            db.commit()
            r=cursor.fetchone()
        except:
            pass
        if r==None:
            c.send(b'No use of this word')
            continue
        else:
            msg = "{} :　{}".format(r[0],r[1])
            c.send(msg.encode())
        def charu(name,l):
            tm = time.ctime()
            sql = "insert into hist (name,word,time) values ('%s','%s','%s')"%(name,l,tm)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
                print('插入历史记录失败!!!')
                return
        charu(name,l)


def chakan(c,db,name):
    print("------历史记录------")
    cursor = db.cursor()
    sql = "select * from hist where name='%s'"%name
    try:
        cursor.execute(sql)
        r = cursor.fetchall()
    except Exception:
        traceback.print_exc()
    if not r:
        c.send(b'FALL')
    else:
        c.send(b'OK')
        r=list(r)
        time.sleep(1)
        c.send(('帐户'+','+'所查单词'+','+'查询时间'+'\n').encode())
        if len(r) > 10:
            r=r[-1:-11:-1]
            for i in r:
                msg = str(i[0])+','+str(i[1])+','+str(i[2])
                c.send(msg.encode())
                time.sleep(0.1)
        else:
            for i in r:
                    msg = str(i[0])+','+str(i[1])+','+str(i[2])
                    c.send(msg.encode())
                    time.sleep(0.1)

        c.send(b'over')
        print("历史记录打印结束")
        



if __name__ == '__main__':
    main()