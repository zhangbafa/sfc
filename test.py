# -*- coding: UTF-8 -*-
import re
import time
import os
from wxpy import *
import sqlite3

#启动机器人
dbpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "sfc.db")
conn = sqlite3.connect(dbpath, check_same_thread=False)



bot = Bot(cache_path=True)
bot.enable_puid()
bot.groups(update=True, contact_only=False)
# 初始化机器人，电脑弹出二维码，用手机微信扫码登陆
bot.groups(update=True, contact_only=False)
boring_group = bot.groups()
print(boring_group)