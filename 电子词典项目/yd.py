import pymysql
import re

###1.创建数据库链接对象
conn = pymysql.connect(host='localhost',user='root',password='123456',database='dict',charset='utf8')
###2.创建游标对象
cursor1=conn.cursor()
###3打开单词文件导入数据库
f=open('all.txt',mode='r',encoding='UTF-8')
for line in f:
    l=re.split(r'[ ]+',line)
    word=l[0]
    interpret=' '.join(l[1:])
    s='insert into words1(word,interpret) values ("%s","%s")'%(word,interpret)
    try:
        cursor1.execute(s)
        conn.commit()
    except:
        conn.rollback()

f.close()