import os

time = input("请输入几秒后关机：")
print("如果你想要取消，请运行shutdown -a")
os.system(f"shutdown -s -t {time} -c 计算机将在{time}秒后关机！")
#author is hydrooxygen
