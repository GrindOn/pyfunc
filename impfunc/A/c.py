"""绝对导入"""
# c.py中导入B包/B1子包/b1.py模块
'''
import sys,os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 存放c.py所在的绝对路径
sys.path.append(BASE_DIR)
from B.B1 import b1  # 导入B包中子包B1中的模块b1

b1.bb1()'''


"""相对导入"""
# 单独导入包

import B
B.B1.b2.bb2()  # 直接运行会报错

#  解决办法：
# B/   init   .py代码添加
# from . import B1  #其中的.表示当前目录

# B/B1/   init   .py代码添加
# from . import b2