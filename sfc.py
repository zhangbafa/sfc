# -*- coding: UTF-8 -*-
import re
import time
import os
from wxpy import *
import sqlite3


'''
抓取微信群中的拼车信息，同步到数据库'''

#启动机器人

bot = Bot(cache_path=True)
bot.groups(update=True, contact_only=False)
# 初始化机器人，电脑弹出二维码，用手机微信扫码登陆
bot.groups(update=True, contact_only=False)
# boring_group = bot.groups().search(u'宿州同乡')[0]
boring_group1 = bot.groups().search(u'老少')[0]
boring_group2 = bot.groups().search(u'栏杆')[0]
boring_group1.update_group(members_details=True)
boring_group2.update_group(members_details=True)

# self.connection = sqlite3.connect(self.database, timeout=3, isolation_level=None,check_same_thread=False)



@bot.register([boring_group1,boring_group2],msg_types="Text",except_self=False)
#注册消息响应事件，一旦收到铲屎群的消息，就执行下面的代码同步消息。机器人自己在群里发布的信息也进行同步。
def sync_my_groups(msg):    
    # sync_message_in_groups(msg, my_groups)
	
	try:
		if  not msg.is_at:
			sender = msg.raw['ActualNickName']
			content = msg.text
			createtime = msg.raw['CreateTime']
			phone = re.findall("1\d{10}", content)
			#1为车找人
			type=0
			if "车找人" in content:
				type=1
			dbpath = os.path.join(os.path.abspath(os.path.dirname(__file__)),"sfc.db")
			conn = sqlite3.connect(dbpath,check_same_thread=False)
			cursor = conn.cursor()
			
			selectsql = "select * from posts where sender=? order by createtime desc limit 1 "
			cursor.execute(selectsql, (sender,))
			result = cursor.fetchone()
			if result == None or createtime-result[4]>60:
				data = [sender, phone[0],content,createtime,type]
				sql = "INSERT INTO posts(sender,phone,content,createtime,type) VALUES(?,?,?,?,?)"
				cursor.execute(sql, data)
				cursor.close()
				conn.commit()
			conn.close()
			print(sender,content,phone,createtime)			
        
	except BaseException as e:
		print(e)
	finally:
		print('%s[%s] : %s [success]' % (sender, dt, phone[0]))
   
embed()