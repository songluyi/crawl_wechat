# -*- coding: utf-8 -*-
# 2016/9/7 13:47
"""
-------------------------------------------------------------------------------
Function:   using for fucking wechat
Version:    1.1
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import multiprocessing
from multiprocessing import Pool as ThreadPool
import string,re,ftplib,time
import requests,pymysql
class fuck_wechat(object):
    def __init__(self):
        self.time=time.strftime("%m_%d_%H_%M_%S", time.localtime())
        self.ID=1
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
    def change_txt(self):
        f=open('Response.txt','r',encoding='gbk',errors='ignore')
        data=f.readlines()
        new_data=[]
        file_write_new=open('New_Response.txt','wb')
        for i in data:
            i=str(i).replace("b'",'').replace("'",'')
            # i.replace('\x00','')
            hope=''.join(list(filter(lambda x: x in string.printable, i)))
            if hope.startswith('#')or not hope.split():
                continue
            file_write_new.write(bytes(hope,encoding='utf-8'))
            # print(bytes(hope,encoding='utf-8'))
        file_write_new.close()
        f.close()
    def return_all_article(self):
        msglist=[]
        start_row=[]
        end_row=[]
#这个continue的list是为了解决微信后来传输json的历史文章页。
        continue_start_row=[]
        continue_end_row=[]
        f=open('New_Response.txt','r',encoding='utf-8',errors='ignore')
        file_data=f.readlines()
        # all_row=len(file_data)
        # print(file_data)
        count=0
        for need_data in file_data:
            count+=1
            if 'msgList' in str(need_data) :
                start_row.append(count)
            if '{"ret":0,' in str(need_data):
                continue_start_row.append(count)
            if 'if(!!window.__initCatch)' in str(need_data)  :
                end_row.append(count)
            if 'csp_nonce_str' in str(need_data):
                continue_end_row.append(count)
        print(start_row)
        print(end_row)
        print(continue_start_row)
        print(continue_end_row)
        all_article=[]
        if start_row:
            for i in range(len(start_row)):
                row_article_list=''.join(file_data[start_row[i-1]:end_row[i]])
                row_article_list=row_article_list.replace('\t','').replace(' ','').replace('&quot;','').replace('&nbsp;','').replace('\\\\','')\
                    .replace('amp;amp;','').replace(',','')
                print(row_article_list)
                result=re.findall("http://mp.weixin.qq.com/s(.*?)#",row_article_list)
                s=list(map(lambda x:'http://mp.weixin.qq.com/s'+x,result))
                all_article.extend(s)
        else:
            print('error：response里面没有历史文章页信息，请检查！')

        if continue_end_row:
            for j in range(len(continue_start_row)):
                row_article_list=''.join(file_data[continue_start_row[j]:continue_end_row[j]])
                row_article_list=row_article_list.replace('\\','').replace('amp;','')
                print(row_article_list)
                result=re.findall("http://mp.weixin.qq.com/s(.*?)#",row_article_list)
                s=list(map(lambda x:'http://mp.weixin.qq.com/s'+x,result))
                all_article.extend(s)
        else:
            print('info：response中 没有后续文章页，如果没有模拟点击过，请忽略！')
        return all_article

    def start_request(self,url):
        try:
            self.ID+=1
            data=requests.get(url)
            data.encoding='utf-8'
            # print(data.text)
            s=data.text
            # print(type(s))
            nick_name=re.findall('var nickname =(.*);',s)[0].replace('"','')
            app_uni=re.findall('var appuin =(.*);',s)[0].replace('"','').replace('||','')
            msg_title=re.findall('var msg_title = (.*);',s)[0].replace('"','')
            msg_desc=re.findall('var msg_desc = (.*);',s)[0].replace('"','')
            publish_time=re.findall('var publish_time = (.*);',s)[0].replace('"','').replace(' ||','').replace(' ','')
            print('Finish one')
            print(url)
            # return {'nick_name':nick_name,'app_uni':app_uni,'msg_title':msg_title,'msg_desc':msg_desc,'msg_url':url,
            #         'publish_time':publish_time}
            return (nick_name,app_uni,msg_title,msg_desc,url,publish_time)
        except TimeoutError:
            return None
        except ConnectionError:
            return None


    def get_max_id(self):
        db = pymysql.connect("localhost","root","070801382","world",port=3308,charset='utf8')
        cursor = db.cursor()
        cursor.execute("SELECT max(id) from wechet_db")
        data = cursor.fetchone()
        if data:
            return data[0]
        else:
            raise ConnectionError
    def insert_db(self,data):
        db = pymysql.connect("localhost","root","070801382","world",port=3308,charset='utf8')
        cursor = db.cursor()
        sql="INSERT INTO wechet_db(nick_name,app_uni,msg_title,msg_desc,msg_url,publish_time) VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql,data)
        db.commit()
if __name__=="__main__":
    start_time=time.time()
    pool = ThreadPool(multiprocessing.cpu_count()*2)
    wtf=fuck_wechat()
    # wtf.get_data_from_ftp
    """
    如果你的点击fiddler生成的response在ftp可以用该方法传输到本目录下
    """
    wtf.change_txt()
    article_lists=wtf.return_all_article()
    print(article_lists)
    print(len(article_lists))
    results=list(pool.map(wtf.start_request,article_lists))
    pool.close()
    pool.join()
    print(results)
    print(len(results))
    end_time=time.time()
    cost = end_time - start_time #time in second
    print('耗时为：')
    print(cost)
    wtf.insert_db(results)#如果你没有设置数据库，可以考虑注释掉这一段。
    print('插入数据库成功')

