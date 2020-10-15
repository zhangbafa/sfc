# coding: utf-8
import re
import time
import os
from wxpy import *
import sqlite3

#顺风车群
groups = ['栏杆','解集往返宿州','宿州同乡交流便民','青春','老少']

#连接数据库
dbpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "sfc.db")
conn = sqlite3.connect(dbpath, check_same_thread=False)
# 初始化机器人，电脑弹出二维码，用手机微信扫码登陆
my_groups=list()
bot = Bot(cache_path=True)
bot.groups(update=True, contact_only=False)

for (index,name)  in enumerate(groups):
	#一些不活跃的群可能无法被获取到，可通过在群内发言，或修改群名称的方式来激活
	try:
		print(name)
		boring_group = bot.groups().search(name)[0]
		boring_group.update_group(members_details=True)
		my_groups.append(boring_group)
	except BaseException as e:
		print("活跃度不足:"+name)

#注册消息响应事件
@bot.register(my_groups,msg_types="Text",except_self=False)
def sync_my_groups(msg):    
    # sync_message_in_groups(msg, my_groups)
	
	try:
		if not msg.is_at:
			sender = msg.raw['ActualNickName']
			content = msg.text
			createtime = msg.raw['CreateTime']
			phone = re.findall("1\d{10}", content)
			wxmsg = sender + ":" + str(createtime)
			print(wxmsg)
			#1为车找人
			type = 1 if "找人" in content else 0

			cursor = conn.cursor()
			selectsql = "select * from posts where sender=? order by createtime desc limit 1 "
			cursor.execute(selectsql, (sender,))
			result = cursor.fetchone()

			if (result == None or (int(createtime)-int(result[4])>300)) and len(content)>11:
				data = [sender, phone[0],content,createtime,type]
				sql = "INSERT INTO posts(sender,phone,content,createtime,type) VALUES(?,?,?,?,?)"
				cursor.execute(sql, data)
				cursor.close()
				conn.commit()
			# conn.close()

			print("*"*20)
			# print(sender,content,phone,createtime)
        
	except BaseException as e:
		print(e)
	finally:
		print('%s[%s] : %s [success]' % (sender, dt, phone[0]))
   
embed()


