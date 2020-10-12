# -*- coding: UTF-8 -*-
import re
import time
import os
from wxpy import *
import sqlite3

#启动机器人
'''
bot = Bot(cache_path=True)
bot.enable_puid()
bot.groups(update=True, contact_only=False)
# 初始化机器人，电脑弹出二维码，用手机微信扫码登陆
bot.groups(update=True, contact_only=False)
boring_group = bot.groups()
boring_group[0].update_group(members_details=True)
boring_group[1].update_group(members_details=True)
boring_group[2].update_group(members_details=True)
boring_group[3].update_group(members_details=True)
boring_group[4].update_group(members_details=True)
boring_group[5].update_group(members_details=True)
boring_group[6].update_group(members_details=True)
boring_group[7].update_group(members_details=True)


# self.connection = sqlite3.connect(self.database, timeout=3, isolation_level=None,check_same_thread=False)



@bot.register(boring_group,except_self=False)
#注册消息响应事件，一旦收到铲屎群的消息，就执行下面的代码同步消息。机器人自己在群里发布的信息也进行同步。
def sync_my_groups(msg):    
    # sync_message_in_groups(msg, my_groups)
    print(msg)
    print(dir(msg))
    print("++++++"*10)
    print(dir(msg.chat))
    print(msg.chat.puid)
    
    # print("puid:"+msg.chat.puid)
    # print(msg.chat.get_avatar("./"+puid+".jpg"))
    print("*"*10)
   
embed()

'''
dbpath = os.path.join(os.path.abspath(os.path.dirname(__file__)),"sfc.db")
conn = sqlite3.connect(dbpath,check_same_thread=False)
cursor = conn.cursor()
sender = "0506"
selectsql = "select * from posts where sender=? order by createtime desc limit 1 "
cursor.execute(selectsql, (sender,))
data = cursor.fetchone()
print(data[4])