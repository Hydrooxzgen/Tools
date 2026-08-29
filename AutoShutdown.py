import os

time = input("请输入几秒后关机：")
os.system(f"shutdown -s -t {time} -c 计算机将在{time}秒后关机！")
#author is hydrooxygen