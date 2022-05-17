"""绝对导入"""
# b1.py中导入b2.py模块
# from B.B1 import b2  # 从B包中的子包B1中导入模块b2,A应该为源根，不然不能进行导入


"""相对导入"""
# from . import b2  # 这种导入方式会报错
import b2
b2.bb2()


def bb1():
    print("bb1ok")