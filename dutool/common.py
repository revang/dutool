import time
import datetime


def now():
    """
    当前时间
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
