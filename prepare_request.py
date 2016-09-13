# -*- coding: utf-8 -*-
# 2016/9/5 10:36
"""
-------------------------------------------------------------------------------
Function:   此工具用于获取截获的微信请求报文
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import chardet,sys
import ftplib
import time
import string
from urllib import request
from _collections import deque
import requests
class Get_Wechat(object):
    def __init__(self):
        self.time=time.strftime("%m_%d_%H_%M_%S", time.localtime())
        self.header=self.set_config()[0]
        self.row_request=self.set_config()[1]
    def get_data_from_ftp(self):
        ftp=ftplib.FTP()
        ftp.connect()
        ftp.login()
        print(ftp.cwd())
        DownLocalFilename="Session.txt"
        f = open(DownLocalFilename, 'wb')
        DownRoteFilename="Session.txt"
        ftp.retrbinary('RETR ' + DownRoteFilename , f.write , 1024)
        f.close()
        ftp.close()
    def Change_Ftp_Txt(self):#传过来是字节流不符合string的解析因此进行修改
        f=open('Sessions.txt','r',encoding='gbk',errors='ignore')
        data=f.readlines()
        new_data=[]
        file_write_new=open('New_Session.txt','wb')
        for i in data:
            i=str(i).replace("b'",'').replace("'",'')
            # i.replace('\x00','')
            hope=''.join(list(filter(lambda x: x in string.printable, i)))
            if hope.startswith('#')or not hope.split():
                continue
            file_write_new.write(bytes(hope,encoding='utf-8'))
        file_write_new.close()

    def set_config(self):
        data=deque(open('New_Session.txt','r'),18)
        header={}
        final_request={}
        form_request=[]
        for i in data:
            print(i)
            if ':' in str(i):
                special_data=str(i).split(':')[1].replace('\n','')
                header[str(i).split(':')[0]]=special_data
            else:
                form_request.append(i)
        if 'CONNECT mp.weixin.qq.com' in header and 'Request header' in header and 'Request body' in header :
            list(map(header.pop,['CONNECT mp.weixin.qq.com','Request header','Request body','Request url','Proxy-Connection']))
            #目前尚不清楚为何没有list map就没有实际效果。。。
        split_request=form_request[0].replace('GET ','').split('&')
        for j in split_request[1:]:
            final_request[str(j).split('=')[0]]=str(j).split('=')[1]
        final_request[split_request[0].split('?')[1].split('=')[0]]=split_request[0].split('?')[1].split('=')[1]
        return [header,final_request]
    def start_request_test(self):
        header=self.header
        print(header)
        url='http://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MzA3ODA5NjgyOA==&uin=MjM3ODE4ODcxMg%3D%3D&key=7b81aac53bd2393dd33aa07750d5189e6ad025e93260f9226ce99f1123681c3e1a6521425204ed0293c7ff7e0e46d9b30805712ed1b1ac86&devicetype=Windows+7&version=62020025&lang=zh_CN&ascene=7&pass_ticket=tqneZzemQw0OsH5VSC1z2VTlN0A8OO4eU0VgGGMf6%2BLyPYb8ZdDef%2FX9mWb2gerS&wx_header=1'
        data=requests.get(url,header)
        data.encoding='utf-8'

        print(data.text)

if __name__=="__main__":
    go=Get_Wechat()
    go.Change_Ftp_Txt()
    go.set_config()
    go.start_request_test()
    #麻痹傻吊微信又换加密方式干！


