"""
    目标：
        1、多线程应用
        2、不同浏览器启动参数
"""
from time import sleep


#函数1 说话
def say(name):
    print(f"你好{name}")
    sleep(5)

#函数2 唱歌
def sing(name):
    print(f"{name} 正在唱歌")
    sleep(5)

# 导包
import threading
# 实例化 线程1 线程2
# args=(参数1,参数2...)
t1 = threading.Thread(target=say, args=("张三",))
t2 = threading.Thread(target=say, args=("李四",))
# 启动线程
t1.start()
t2.start()