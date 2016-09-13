# -*- coding: utf-8 -*-
# 2016/9/5 10:57
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

# import string
# f=open('Sessions.txt','r',encoding='gbk',errors='ignore')
# data=f.readlines()
# new_data=[]
# file_write_new=open('New_Session.txt','wb')
# for i in data:
#     i=str(i).replace("b'",'').replace("'",'')
#     # i.replace('\x00','')
#     hope=''.join(list(filter(lambda x: x in string.printable, i)))
#     hope.replace('\n\n','')
#     print(hope)
#     file_write_new.write(bytes(hope,encoding='utf-8'))
# file_write_new.close()


# f=open('New_Session.txt','r',encoding='utf-8')
# data=f.readlines()
# for line in data:
#     if line.startswith('#')or not line.split():
#         continue
#     print(line)
#
# import string
# f=open('Sessions.txt','r',encoding='gbk',errors='ignore')
# data=f.readlines()
# new_data=[]
# file_write_new=open('New_Session.txt','wb')
# for i in data:
#     i=str(i).replace("b'",'').replace("'",'')
#     # i.replace('\x00','')
#     hope=''.join(list(filter(lambda x: x in string.printable, i)))
#     if hope.startswith('#')or not hope.split():
#         continue
#     file_write_new.write(bytes(hope,encoding='utf-8'))
# file_write_new.close()
#
# from _collections import deque
# data=deque(open('New_Session.txt','r'),18)
# header={}
# final_request={}
# form_request=[]
# for i in data:
#     print(i)
#     if ':' in str(i):
#         special_data=str(i).split(':')[1].replace('\n','')
#         print(special_data)
#         header[str(i).split(':')[0]]=special_data
#     else:
#         form_request.append(i)
# if 'CONNECT mp.weixin.qq.com' in header and 'Request header' in header and 'Request body' in header :
#     list(map(header.pop,['CONNECT mp.weixin.qq.com','Request header','Request body']))
#     #目前尚不清楚为何没有list map就没有实际效果。。。
# split_request=form_request[0].replace('GET ','').split('&')
# print(split_request)
# for j in split_request[1:]:
#     if '=' in j:
#         final_request[str(j).split('=')[0]]=str(j).split('=')[1]
# final_request[split_request[0].split('?')[1].split('=')[0]]=split_request[0].split('?')[1].split('=')[1]
# print([header,final_request])
# for i in data:
# import string
# f=open('Sessions.txt','r',encoding='gbk',errors='ignore')
# data=f.readlines()
# new_data=[]
# file_write_new=open('New_Session.txt','wb')
# for i in data:
#     i=str(i).replace("b'",'').replace("'",'')
#     # i.replace('\x00','')
#     hope=''.join(list(filter(lambda x: x in string.printable, i)))
#     if hope.startswith('#')or not hope.split():
#         continue
#     file_write_new.write(bytes(hope,encoding='utf-8'))
# file_write_new.close()


# import requests,re
# url='http://mp.weixin.qq.com/s?__biz=MzA4NzM5ODgxNQ==&mid=2651261830&idx=3&sn=e147edbd414705ccce9890620ab4f3ed&scene=4'
# data=requests.get(url)
# data.encoding='utf-8'
# print(data.text)
# s=data.text
# print(type(s))
# nick_name=re.findall('var nickname =(.*);',s)[0].replace('"','')
# app_uni=re.findall('var appuin =(.*);',s)[0].replace('"','')
# msg_title=re.findall('var msg_title = (.*);',s)[0].replace('"','')
# msg_desc=re.findall('var msg_desc = (.*);',s)[0].replace('"','')
# publish_time=re.findall('var publish_time = (.*);',s)[0].replace('"','').replace(' ||','')



# import logging
# logging.basicConfig(level=logging.DEBUG,
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='myapp.log',
#                 filemode='w')
# import pymysql
# # 打开数据库连接
# db = pymysql.connect("localhost","root","070801382","world",port=3308,charset='utf8')
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # cursor.execute('SET NAMES "utf8"')
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT max(id) from wechet_db")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print(data[0])
#
# # 关闭数据库连接
# db.close()



# import pymysql
# data=[(' 微醺之美', ' MzA3ODA5NjgyOA==', '点击这里关注我们&nbsp;&nbsp;&nbsp;↓↓↓↓↓', '【微醺之美】id:weixunzhimei主讲烈酒鸡尾酒和葡萄酒，偶尔讲讲酒吧餐厅。深', 'http://mp.weixin.qq.com/s?__biz=MzA3ODA5NjgyOA==&mid=200113055&idx=1&sn=0581952a4acba0c54fcafe3d20cbeedc', '2014-03-28'),
# (' 微醺之美', ' MzA3ODA5NjgyOA==', '闪购：如果要和父亲喝葡萄酒，我会选择这一款', '中秋选酒第三弹，适合和家人同享的葡萄酒。', 'http://mp.weixin.qq.com/s?__biz=MzA3ODA5NjgyOA==&mid=2650764592&idx=1&sn=98b9a2843c8fd908c57ab688c143518d&scene=4', '2016-08-24')]
# db = pymysql.connect("localhost","root","070801382","world",port=3308,charset='utf8')
# cursor = db.cursor()
# # cursor.executemany("INSERT INTO wechet_db VALUES (:nick_name,:app_uni,:msg_title,:msg_desc,:msg_url,to_date(:publish_time,'yyyy-mm-dd'))",data)
# sql="INSERT INTO wechet_db(nick_name,app_uni,msg_title,msg_desc,msg_url,publish_time) VALUES(%s,%s,%s,%s,%s,%s)"
# cursor.executemany(sql,data)
# db.commit()
# print('success')