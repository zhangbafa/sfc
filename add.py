# coding: utf-8
import re
import time
import os
from wxpy import *




bot = Bot(cache_path=True)
bot.groups(update=True, contact_only=False)

my_group = bot.groups().search(u'老少')[0]
# my_group.add_all()
print(my_group)
for i in my_group:
	print(i.add())
embed()

'''
def action():
    bot.file_helper.send()

# 执行检测
result = detect_freq_limit(action)
'''


