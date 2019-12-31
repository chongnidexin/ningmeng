import os
# 拓展一：Python可否强制删除
# 拓展二：怎么去新建文件open删除文件

#路径的获取1   获取当前工作目录
path = os.getcwd()
print(path)

#路径获取2    获取当前文件的绝对路径
path_2 = os.path.realpath(__file__)
print(path_2)

#第三个知识点：拼接路径
#拼接路径1:
new_path = os.getcwd()+"\\xxx"
print(new_path)
#拼接路径2：
new_path_2 = os.path.join(os.getcwd(),"xxxx","xxxx")
print(new_path_2)

#判断是否是文件
print(os.path.isfile(os.getcwd()))
#判断是否是文件夹
print(os.path.isdir(os.getcwd()))
#判断文件是否存在
print(os.path.exists("D:\\work\\practice\ningmeng\new_path.py"))
#罗列出当前路径的所有文件和目录
print(os.listdir(os.getcwd()))



#拓展题目
#给定一个路径，请打印出所有的路径
#思路：递归函数 
for path in os.listdir(os.getcwd()):
	if os.path.isdir(path):
		os.listdir(os.path.join(os.getcwd(),path))
		print("{}还需要进一步处理".formart(path))
	else:
		print("这是一个穷尽的路径",os.path.join(os.getcwd(),path))