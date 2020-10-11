# -*- coding: UTF-8 -*-
import re
import pymysql
import subprocess
import time
import os
from wxpy import *


'''
抓取微信群中的拼车信息，同步到数据库
'''
# my_groups = []
#启动机器人
bot = Bot(cache_path=True)
bot.groups(update=True, contact_only=False)

# 初始化机器人，电脑弹出二维码，用手机微信扫码登陆
bot.groups(update=True, contact_only=False)
#微信登陆后，更新微信群列表（包括未保存到通讯录的群）

# my_groups[0].update_group(members_details=True)

# my_groups1=bot.groups().search(u'宿州同乡')
# my_groups[1].update_group(members_details=True)

# my_groups2=bot.groups().search(u'栏杆')
# my_groups2[0].update_group(members_details=True)

boring_group = bot.groups().search(u'宿州同乡')[0]
boring_group1 = bot.groups().search(u'老少')[0]
boring_group2 = bot.groups().search(u'栏杆')[0]


@bot.register([boring_group,boring_group1,boring_group2], except_self=False)
#注册消息响应事件，一旦收到铲屎群的消息，就执行下面的代码同步消息。机器人自己在群里发布的信息也进行同步。
def sync_my_groups(msg):
    print(msg)
    # sync_message_in_groups(msg, my_groups)
    #同步2个群的消息。包括文字、图片、视频、语音、文件、分享、普通表情、地图等。
embed()
#堵塞线程，让机器人保持运行 
'''
@bot.register(my_groups, except_self=False)
#注册消息响应事件，一旦收到铲屎群的消息，就执行下面的代码同步消息。机器人自己在群里发布的信息也进行同步。
def sync_my_groups(msg):
    
    try:
        sender = msg.raw['ActualNickName']
        content = msg.text
        createtime = msg.raw['CreateTime']
        phone = re.findall("1\d{10}", content)
        print(sender,content,phone,createtime)
        # if phone[0] not in black_list and len(content)>11:
        #     insert_mysql(content, phone[0],createtime)
        # else:
        #     print '黑名单[%s]' % (sender,)
        mp3 = '/Users/zhang1/Desktop/pconline1552894436041.wav'
        subprocess.Popen(['mplayer', '-really-quiet', mp3])
        dt = time.strftime("%Y-%m-%d %H:%M:%S",createtime)
        print('%s[%s] : %s [success]' % (sender, dt, phone[0]))
    except:
        pass
    finally:
        print ('%s[%s] : %s [success]' % (sender, dt, phone[0]))
  
    # sync_message_in_groups(msg, my_groups)
    #同步“铲屎官1群”和“铲屎官2群”的消息。包括文字、图片、视频、语音、文件、分享、普通表情、地图等。
# bot.join()
embed()'''
