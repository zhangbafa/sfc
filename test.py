# -*- coding: UTF-8 -*-
import re
import time
import os
from wxpy import *
import sqlite3

#启动机器人
groups = ['栏杆','解集往返宿州','老少爷们','青春共聚','同乡交流']
'''
抓取微信群中的拼车信息，同步到数据库'''

#启动机器人

my_groups=list()
bot = Bot(cache_path=True)
bot.groups(update=True, contact_only=False)
print(bot.groups())
# 初始化机器人，电脑弹出二维码，用手机微信扫码登陆
# for (index,name)  in enumerate(groups):
#     print((name))
    
#     boring_group= bot.groups().search(name)[0]
#     boring_group.update_group(members_details=True)
#     my_groups.append(boring_group)

# embed()