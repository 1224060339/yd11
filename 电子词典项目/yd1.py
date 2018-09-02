import pymysql
import re

###1.创建数据库链接对象
conn = pymysql.connect(host='localhost',user='root',password='123456',database='dict')
###2.创建游标对象
cursor1=conn.cursor()
###3打开单词文件导入数据库
f=open('dict.txt')
for line in f:
    l=re.split(r'[ ]+',line)
    word=l[0]
    interpret=' '.join(l[1:])
    s='insert into words (word,interpret) values ("%s","%s")'%(word,interpret)
    try:
        cursor1.execute(s)
        conn.commit()
    except:
        conn.rollback()

f.close()




# f=open('dict.txt')
# while True:
#     s=input()
#     for line in f:
#         x=line.split(' ')[0]
#         if x>s:
#             break
#         if s==x:
#             print(line)