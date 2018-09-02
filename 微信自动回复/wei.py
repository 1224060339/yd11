from __future__ import unicode_literals
#coding = utf-8

import sys
import os

import requests
import pymysql
import itchat
from itchat.content import *

# 图灵机器人网站接口
APIUIL = 'http://www.tuling123.com/openapi/api'


@itchat.msg_register([TEXT])
def simple_reply(msg):
    print(NickNamedict[msg['FromUserName']], ':', msg['Text'])
    # 如果消息是自己发来的
    if msg['FromUserName'] == myUserName:
        # 使用命令执行函数处理自己发来的命令
        command(msg)
    # 如果消息是好友发来的
    else:
        # 使用消息回复函数处理并回复好好友发来的消息
        Reply(msg)

# 消息回复函数


def Reply(msg):
    # 将收到的消息写入数据库,此处用列表暂时代替
    sql.run(
        'insert into msg(NickName,Msg) value("%s","%s");' % (NickNamedict[msg['FromUserName']], '好友说:' + msg['Text']))
    if msg['Text'] == '关闭自动回复':
        back_msg = swit.break_switch(NickNamedict[msg['FromUserName']])
        itchat.send_msg(back_msg, msg['FromUserName'])
        return
    if msg['Text'] == '开启自动回复':
        back_msg = swit.open_switch(NickNamedict[msg['FromUserName']])
        itchat.send_msg(back_msg, msg['FromUserName'])
        return
    if swit.switch_type(NickNamedict[msg['FromUserName']]):
        # 发送返回消息给好友
        send_data = msg['Text']
        # 发送给图灵机器人,并接收返回消息
        APIdata = {
            'key': 'ac78a3cd42b94fafae6158fa851afd7b',  # 这是我自己图灵机器人密钥,你也可以免费申请一个
            'info': send_data,  # 这是我们发出去的消息
            'userid': 'wechat-robot',  # 这里你想改什么都可以
        }
        back_msg = requests.post(APIUIL, data=APIdata).json()['text']
        # 将消息发送给好友
        back_msg_ending = '\n 【本人正在上课,这是由机器人回复的一条消息,可以回复"关闭自动回复"停止与机器人交谈.】'
        itchat.send_msg(back_msg + back_msg_ending, msg['FromUserName'])
        print('回复:', back_msg)
        # 将返回消息写入数据库,此处仍用列表代替
        sql.run(
            'insert into msg(NickName,Msg) value("%s","%s");' % (NickNamedict[msg['FromUserName']], '机器人说:' + back_msg))


# 命令执行函数
def command(s):
    try:
        if s['Text'] == '关闭自动回复':
            swit.break_myswitch()
            itchat.send_msg('自动回复功能已关闭', toUserName='filehelper')
        elif s['Text'] == '开启自动回复':
            swit.open_myswitch()
            itchat.send_msg('自动回复功能已开启', toUserName='filehelper')
        elif s['Text'] == '关闭程序':
            itchat.logout()
            sys.exit('收到远程命令,退出程序')
        elif s['Text'] == '关机':
            os.system('shutdown -h now')
        else:
            itchat.send_msg('识别不了的命令.', toUserName='filehelper')
    except Exception as e:
        itchat.send_msg('执行命令时发生了错误', toUserName='filehelper')


# 数据库对象
class sqlserver():

    def __init__(self):
        try:
            # 连接数据库
            self.conn = pymysql.connect(host="MySQL数据库地址",
                                        user="数据库用户名", password="数据库的密码",
                                        database="储存消息的数据库", charset="utf8")  # 此处需自己添加自己的数据库数据
            # 关闭事务功能,立即提交sql语句
            self.conn.autocommit(True)
            # 创建游标对象
            self.cursor = self.conn.cursor()
        except Exception as e:
            sys.exit('连接数据库失败,退出程序.')

    def run(self, sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 执行后立即提交
        except Exception as e:
            print('执行sql语句失败,错误信息为:', e)
    # 删除数据库对象时自动关闭数据库游标

    def __del__(self):
        self.cursor.close()
        self.conn.close()

# 回复开关对象


class switch():

    def __init__(self):
        self.off_NickName = []
        # 读取关闭自动回复用户的列表#暂用文件表示
        sql.run('select NickName from off;')
        for i in sql.cursor.fetchall():
            for j in i:
                self.off_NickName.append(j)
        # 开启程序,自动回复开关默认开启
        self.myswitch = True

    # 获取单个用户自动回复的状态
    def switch_type(self, NickName):
        # 如果系统自动回复在打开状态
        if self.myswitch:
            # 如果在列表内
            if NickName in self.off_NickName:
                return False
            # 如果不在列表内
            else:
                return True
        return False

    # 开启单个用户的自动回复.并返回提示语句
    def open_switch(self, NickName):
        # 如果用户在关闭清单内,从数据库中删除该用户,并重新读取数据库,更新关闭清单
        if NickName in self.off_NickName:
            sql.run('delete from off where NickName="%s"' % NickName)
            self.off_NickName.remove(NickName)
            return '您成功开启了自动回复功能,开始畅聊吧!'
        # 如果用户自动回复已经在开启状态,返回一局提示消息
        else:
            return '您已经开启过自动回复了'

    # 关闭单个用户的自动回复
    def break_switch(self, NickName):
        # 如果用户自动回复已经在关闭状态,返回一句提示消息
        if NickName in self.off_NickName:
            return '自动回复您已经关闭过了,无需重复操作'
        # 如果用户的自动回复不在关闭清单内,加入数据库,并重新加载清单列表
        else:
            sql.run('insert into off(NickName) value("%s");' % NickName)
            self.off_NickName.append(NickName)
            return '您已关闭了自动回复,可以回复"开启自动回复"重新开启功能!'

    # 关闭系统自动回复开关
    def break_myswitch(self):
        self.myswitch = False

    # 开启系统自动回复开关
    def open_myswitch(self):
        self.myswitch = True


if __name__ == '__main__':
    # 连接MySQL服务器,创建服务器对象
    sql = sqlserver()
    # 创建开关对象
    swit = switch()
    # 登陆,退出程序后暂留登陆信息
    itchat.auto_login(hotReload=True)
    # 获取好友信息的字典
    myself = itchat.get_friends()
    # 将UserName作为键,NickName作为值放入字典中,方便查找NickName
    NickNamedict = {}
    for i in myself:
        NickNamedict.update({i['UserName']: i['NickName']})
    # 获取自己的UserName
    myUserName = myself[0]["UserName"]
    # 运行
    itchat.run()
